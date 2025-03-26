from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
def tasks(request):
    return HttpResponse("Hello, DoodleTo tasks!")


@login_required
def board(request):
    """
    Renders a task board view, categorizing tasks by their status.

    This view retrieves all tasks from the database, orders them based on
    a query parameter, and filters them into three categories: Pending,
    In Progress, and Completed. The categorized tasks are then passed to the
    template for rendering.

    Args:
        request (HttpRequest): The HTTP request object containing metadata
        about the request, including GET parameters.

    Returns:
        HttpResponse: A rendered HTML page displaying tasks grouped by their
        status (Pending, In Progress, Completed).
    """
    tasks = Task.objects.filter(user=request.user)
    tasks = Task.objects.order_by("due_date")

    pending = tasks.filter(status="P")
    in_progress = tasks.filter(status="IP")
    completed = tasks.filter(status="C")

    return render(request, "** insert template **", {
        "tasks": tasks,  # May not be needed
        "pending": pending,
        "in_progress": in_progress,
        "completed": completed,
    })
