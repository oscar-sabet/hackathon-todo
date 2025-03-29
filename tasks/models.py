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
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    CATEGORY_CHOICES = [
        ("Work", "Work"),
        ("Personal", "Personal"),
        ("Home", "Home"),
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
        default='Pending'
        )
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default="Medium"
        )
    category = models.CharField(
        max_length=8,
        choices=CATEGORY_CHOICES,
        default="Personal"
        )

    def __str__(self):
        return self.title
