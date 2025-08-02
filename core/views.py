from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer
from .models import User
from .moodle import create_moodle_user

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


class ActivateUserView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            return Response({"detail": "Invalid activation link."}, status=400)

        if default_token_generator.check_token(user, token):
            if not user.is_active:
                user.is_active = True
                user.save()

                try:
                    print("#" * 200)
                    print(user.password)
                    print("#" * 200)
                    moodle_user_id = create_moodle_user(user, user.password)
                    user.moodle_user_id = moodle_user_id
                    user.save()
                except Exception as e:
                    return Response(
                        {"detail": f"Activated, but Moodle error: {str(e)}"},
                        status=500,
                    )
            return Response({"message": "Account activated successfully."})
        else:
            return Response({"detail": "Invalid or expired token."}, status=400)
