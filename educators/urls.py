from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

router = DefaultRouter()
router.register(r"teachers/courses", CourseViewSet, basename="teacher-courses")

urlpatterns = router.urls
