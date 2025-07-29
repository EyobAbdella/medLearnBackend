from .models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "cme_credits",
            "price",
            "thumbnail",
            "moodle_course_id",
            "created_at",
            "published",
        ]
        read_only_fields = ["moodle_course_id", "created_at"]

    def create(self, validated_data):
        user = self.context["user"]
        if user.role != "teacher":
            raise serializers.ValidationError("Only teachers can create courses.")
        validated_data["teacher"] = user
        print("Creating course with data:", validated_data)
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context["user"]
        if instance.teacher != user:
            raise serializers.ValidationError("You can only edit your own course.")
        return super().update(instance, validated_data)
