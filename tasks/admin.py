from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "category",
        "user",
        "created",
        "due_date",
        "completed_date",
    )
    list_filter = ("status", "priority", "category", "user")
    search_fields = ("title", "description")
