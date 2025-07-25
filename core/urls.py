from django.urls import path
from .views import SignupView, LoginView

urlpatterns = [
    # Signup URLs (admin excluded)
    path("student/signup/", SignupView.as_view(), name="student-signup"),
    path("teacher/signup/", SignupView.as_view(), name="teacher-signup"),
    path("manager/signup/", SignupView.as_view(), name="manager-signup"),
    # Login URLs (including admin)
    path("student/login/", LoginView.as_view(), name="student-login"),
    path("teacher/login/", LoginView.as_view(), name="teacher-login"),
    path("manager/login/", LoginView.as_view(), name="manager-login"),
    path("admin/login/", LoginView.as_view(), name="admin-login"),
]
