from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = "admin"
    MANAGER = "manager"
    TEACHER = "teacher"
    STUDENT = "student"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (MANAGER, "Manager"),
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    scfhs_id = models.IntegerField(null=True, blank=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.email} ({self.role})"

    def is_admin(self):
        return self.role == self.ADMIN

    def is_manager(self):
        return self.role == self.MANAGER

    def is_teacher(self):
        return self.role == self.TEACHER

    def is_student(self):
        return self.role == self.STUDENT
