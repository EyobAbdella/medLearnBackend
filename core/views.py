from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer

ALLOWED_ROLES = {"student", "teacher", "manager"}
ALL_ROLES = {"student", "teacher", "manager", "admin"}


class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        view_name = request.resolver_match.view_name
        role = view_name.split("-")[0]

        if role not in ALLOWED_ROLES:
            return Response({"detail": "Signup not allowed for this role."}, status=403)

        try:
            validate_password(request.data.get("password"))
        except ValidationError as e:
            return Response(
                {"password": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SignupSerializer(data=request.data, context={"role": role})
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": f"{role.capitalize()} registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        view_name = request.resolver_match.view_name
        role = view_name.split("-")[0]

        if role not in ALL_ROLES:
            return Response({"detail": "Invalid role."}, status=400)

        serializer = LoginSerializer(data=request.data, context={"role": role})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=400)
