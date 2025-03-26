from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone
# from cloudinary.models import CloudinaryField


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("P", "Pending"),
        ("IP", "In Progress"),
        ("C", "Completed"),
    ]

    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    ]

    CATEGORY_CHOICES = [
        ("W", "Work"),
        ("P", "Personal"),
        ("H", "Home"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default="P"
        )
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default="M"
        )
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default="P"
        )
