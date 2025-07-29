from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return courses created by the logged-in teacher
        if self.request.user.role != "teacher":
            raise PermissionDenied("Only teachers can access this.")
        return Course.objects.filter(teacher=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign teacher
        if self.request.user.role != "teacher":
            raise PermissionDenied("Only teachers can create courses.")
        serializer.save(teacher=self.request.user)

    def perform_update(self, serializer):
        # Prevent editing others’ courses
        if self.get_object().teacher != self.request.user:
            raise PermissionDenied("You can only update your own courses.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.teacher != self.request.user:
            raise PermissionDenied("You can only delete your own courses.")
        instance.delete()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
