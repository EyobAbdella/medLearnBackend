from django.http import HttpResponse
from django.db.models import Sum, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from .models import Cart, CartItem, Course, Order
from .serializers import (
    CartItemSerializer,
    CartSerializer,
    CourseSerializer,
    OrderCreateSerializer,
    OrderSerializer,
)
from .permissions import IsCourseEditor
import pandas as pd
from io import BytesIO


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsCourseEditor]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = []
    search_fields = ["title", "description"]
    ordering_fields = ["price", "cme_credits", "created_at"]
    ordering = ["-created_at"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    @action(detail=False, methods=["get"], url_path="my-courses")
    def my_courses(self, request):
        if request.user.is_authenticated:
            courses = Course.objects.filter(created_by=request.user)
            serializer = self.get_serializer(courses, many=True)
            return Response(serializer.data)
        raise PermissionDenied("Login required to access your courses.")


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ["get"]

    def get_queryset(self):
        course_id = self.kwargs.get("course_pk")
        queryset = Order.objects.select_related("course").filter(course_id=course_id)

        start_date = self.request.query_params.get("start")
        end_date = self.request.query_params.get("end")

        if start_date:
            queryset = queryset.filter(created_at__date__gte=parse_date(start_date))
        if end_date:
            queryset = queryset.filter(created_at__date__lte=parse_date(end_date))

        return queryset

    @action(detail=False, methods=["get"])
    def analytics(self, request, course_pk=None):
        orders = self.get_queryset()

        revenue = orders.aggregate(total=Sum("course__price_after"))["total"] or 0
        order_count = orders.count()

        top_courses = (
            orders.values("course__title")
            .annotate(total_sales=Count("id"), revenue=Sum("course__price_after"))
            .order_by("-total_sales")[:5]
        )

        return Response(
            {
                "revenue": revenue,
                "order_count": order_count,
                "top_courses": list(top_courses),
            }
        )

    @action(detail=False, methods=["get"])
    def export_excel(self, request, course_pk=None):
        orders = self.get_queryset()
        df = pd.DataFrame(
            [
                {
                    "Course": o.course.title,
                    "Price": o.course.price_after,
                    "Date": o.created_at.date(),
                    "Buyer": o.user.email,
                }
                for o in orders
            ]
        )
        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)
        response = HttpResponse(buffer, content_type="application/vnd.ms-excel")
        response["Content-Disposition"] = "attachment; filename=orders_report.xlsx"
        return response

    @action(detail=False, methods=["get"])
    def export_pdf(self, request, course_pk=None):
        orders = self.get_queryset()
        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 800, "Orders Report")
        y = 770
        for o in orders:
            line = f"{o.created_at.date()} - {o.course.title} = ${o.course.price_after} (by {o.user.email})"
            p.drawString(50, y, line)
            y -= 20
            if y < 50:
                p.showPage()
                y = 800
        p.save()
        buffer.seek(0)
        return HttpResponse(buffer, content_type="application/pdf")


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_cart(self):
        cart_id = self.kwargs["cart_pk"]
        try:
            cart = Cart.objects.get(pk=cart_id, user=self.request.user)
        except Cart.DoesNotExist:
            raise PermissionDenied("Invalid cart or permission denied.")
        return cart

    def get_queryset(self):
        cart = self.get_cart()
        return CartItem.objects.filter(cart=cart)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["cart"] = self.get_cart()
        return context


class OrderViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializer
        return OrderSerializer

    def create(self, request):
        serializer = OrderCreateSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        orders = serializer.save()
        response_serializer = OrderSerializer(
            orders, many=True, context={"request": request}
        )
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
