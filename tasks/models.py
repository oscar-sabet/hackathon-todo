from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.utils import timezone
# from cloudinary.models import CloudinaryField


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # Ensure this line is indented properly

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
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
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

    def __str__(self):
        return self.title
