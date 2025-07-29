from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsCourseEditor


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
