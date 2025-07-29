from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserManagementSerializer
from rest_framework.permissions import IsAdminUser

User = get_user_model()


class UserManagementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserManagementSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.all()
