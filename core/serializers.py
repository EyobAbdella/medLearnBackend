from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "scfhs_id"]

    def create(self, validated_data):
        role = self.context.get("role")
        validated_data["role"] = role
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        role = self.context.get("role")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        if not user.is_active:
            raise serializers.ValidationError("Account disabled")

        if role and user.role != role:
            raise serializers.ValidationError(f"This is not a {role} account")

        refresh = RefreshToken.for_user(user)
        return {
            "email": user.email,
            "role": user.role,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
