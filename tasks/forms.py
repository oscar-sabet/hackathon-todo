from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "due_date",
            "priority",
            "category",
            "status"
            ]
        exclude = ["user", "created", "completed_date"]
        widgets = {
            "due_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "description": forms.Textarea(
                attrs={
                    "cols": 25,
                    "placeholder": "Enter task description here",
                }
            ),
        }
