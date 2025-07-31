from django.db import models
from django.conf import settings
from uuid import uuid4


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role__in": ["admin", "manager", "teacher"]},
        related_name="courses",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cme_credits = models.DecimalField(max_digits=4, decimal_places=1)
    price_before = models.DecimalField(max_digits=8, decimal_places=2)
    price_after = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.ImageField(upload_to="course_thumbnails/")
    course_id = models.PositiveIntegerField(unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart ({self.user.username})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("cart", "course")
