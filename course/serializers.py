from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.email")

    class Meta:
        model = Course
        fields = [
            "id",
            "created_by",
            "title",
            "slug",
            "description",
            "cme_credits",
            "price",
            "thumbnail",
            "course_id",
            "created_at",
            "published",
        ]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        user = self.context["user"]
        if user.role not in ["admin", "manager", "teacher"]:
            raise serializers.ValidationError(
                "You are not authorized to create courses."
            )
        validated_data["created_by"] = user
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context["user"]

        if user.role != "admin" and instance.created_by != user:
            raise serializers.ValidationError("You can only edit your own course.")

        if "thumbnail" not in self.initial_data:
            validated_data["thumbnail"] = instance.thumbnail

        return super().update(instance, validated_data)
