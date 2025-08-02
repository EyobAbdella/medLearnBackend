from django.db import transaction
from rest_framework import serializers
from .models import Cart, CartItem, Category, Course, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CourseSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.email")
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "created_by",
            "title",
            "slug",
            "description",
            "category",
            "price_before",
            "price_after",
            "cme_credits",
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


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "course",
            "created_at",
            "status",
            "complaint",
            "complaint_status",
            "refund_requested",
            "refund_approved",
        ]
        read_only_fields = ["created_at", "user", "refund_approved", "complaint_status"]

    def create(self, validated_data):
        user = self.context["user"]
        validated_data["user"] = user
        return Order.objects.create(**validated_data)


class OrderCreateSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField(write_only=True)

    def validate_cart_id(self, cart_id):
        user = self.context["request"].user
        try:
            cart = Cart.objects.prefetch_related("items__course").get(
                pk=cart_id, user=user
            )
        except Cart.DoesNotExist:
            raise serializers.ValidationError(
                "Cart does not exist or does not belong to you."
            )
        if not cart.items.exists():
            raise serializers.ValidationError("Cart is empty.")
        return cart_id

    def create(self, validated_data):
        user = self.context["request"].user
        cart_id = validated_data["cart_id"]
        cart = Cart.objects.prefetch_related("items__course").get(pk=cart_id, user=user)

        with transaction.atomic():
            orders = []
            for item in cart.items.all():
                order = Order.objects.create(
                    user=user,
                    course=item.course,
                )
                orders.append(order)

            cart.items.all().delete()
            cart.delete()
        return orders


class CartItemSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "course", "course_id"]

    def create(self, validated_data):
        # `course_id` is passed in as part of validated_data
        course = Course.objects.get(id=validated_data["course_id"])
        cart = self.context["cart"]  # passed from view via serializer context

        # Prevent duplicates (optional – safe since you have unique_together)
        existing = CartItem.objects.filter(cart=cart, course=course).first()
        if existing:
            raise serializers.ValidationError("Course already in cart.")

        return CartItem.objects.create(cart=cart, course=course)


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "created_at", "items"]
        read_only_fields = ["user"]
