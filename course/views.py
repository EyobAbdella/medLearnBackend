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
    filterset_fields = [
        "status",
        "course__title",
        "user__email",
        "complaint_status",
        "refund_requested",
        "refund_approved",
    ]

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

    @action(detail=False, methods=["get"])
    def abandoned_orders(self, request, course_pk=None):
        """List orders that are stuck (not completed)"""
        orders = self.get_queryset().filter(
            status__in=["pending", "processing", "learning"]
        )
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def resolve_complaint(self, request, pk=None):
        """Admin resolves or rejects a complaint"""
        order = self.get_object()
        action = request.data.get("action")

        if action == "resolve":
            order.complaint_status = "resolved"
        elif action == "reject":
            order.complaint_status = "rejected"
        else:
            return Response({"detail": "Invalid action"}, status=400)

        order.save()
        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=["patch"])
    def approve_refund(self, request, pk=None):
        """Admin approves refund and cancels course"""
        order = self.get_object()
        if not order.refund_requested:
            return Response({"detail": "No refund requested."}, status=400)

        order.refund_approved = True
        order.status = "canceled"
        order.save()
        # TODO: Integrate with payment gateway or trigger webhook

        return Response(OrderSerializer(order).data)


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
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.select_related("course").filter(user=self.request.user)

    @action(detail=True, methods=["get"])
    def course_progress(self, request, pk=None):
        order = self.get_object()

        if order.status == "completed":
            return Response(
                {
                    "course_title": order.course.title,
                    "status": "completed",
                    "message": "CME registration completed",
                }
            )

        if order.status == "learning":
            return Response(
                {
                    "course_title": order.course.title,
                    "status": "learning",
                    "action": "start_course",
                    "moodle_url": f"https://moodle.yourdomain.com/course/{order.course.id}",
                }
            )

        return Response(
            {
                "course_title": order.course.title,
                "status": order.status,
                "message": "Your course has not started yet.",
            }
        )

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

    @action(detail=True, methods=["post"])
    def submit_complaint(self, request, pk=None):
        order = self.get_object()
        complaint = request.data.get("complaint", "").strip()

        if not complaint:
            return Response({"detail": "Complaint text is required."}, status=400)

        order.complaint = complaint
        order.complaint_status = "submitted"
        order.save()
        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=["post"])
    def request_refund(self, request, pk=None):
        order = self.get_object()

        if order.status == "completed":
            return Response(
                {"detail": "Completed orders cannot be refunded."}, status=400
            )

        order.refund_requested = True
        order.save()
        return Response(OrderSerializer(order).data)
