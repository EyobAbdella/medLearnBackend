from django.db import models
from django.conf import settings


class Course(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "teacher"},
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    cme_credits = models.DecimalField(max_digits=4, decimal_places=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.ImageField(upload_to="course_thumbnails/")
    moodle_course_id = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
