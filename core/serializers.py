from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .moodle import create_moodle_user


def send_activation_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    activation_link = f"{settings.FRONTEND_URL}/activate/{uid}/{token}/"

    send_mail(
        subject="Activate your account",
        message=f"Hi {user.first_name},\nPlease activate your account:\n{activation_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "scfhs_id",
            "city",
            "country",
        ]

    def create(self, validated_data):
        role = self.context.get("role")
        validated_data["role"] = role
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)

        # try:
        #     moodle_user_id = create_moodle_user(user, password)
        #     user.moodle_user_id = moodle_user_id
        # except Exception as e:
        #     raise serializers.ValidationError(
        #         {"moodle": f"Failed to register on Moodle: {str(e)}"}
        #     )

        user.save()
        send_activation_email(user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        role = self.context.get("role")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")

        if not user.is_active:
            raise serializers.ValidationError(
                "Your account is not activated. Please check your email to activate."
            )
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid username or password")

        if not user.is_active:
            raise serializers.ValidationError("Account is disabled")

        if role and user.role != role:
            raise serializers.ValidationError(f"This is not a {role} account")

        refresh = RefreshToken.for_user(user)
        return {
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
