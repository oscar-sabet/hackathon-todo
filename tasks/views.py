from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required


# Display the list of tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Add a new task
def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            Task.objects.create(title=task_title)
        return redirect('task_list')
    return render(request, 'add_task.html')

# Mark a task as completed
def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# Delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


# @login_required
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
    # tasks = Task.objects.filter(user=request.user)
    tasks = Task.objects.order_by("due_date")

    pending = tasks.filter(status="P")
    in_progress = tasks.filter(status="IP")
    completed = tasks.filter(status="C")

    return render(request, "tasks/projectboard.html", {
        "tasks": tasks,  # May not be needed
        "pending": pending,
        "in_progress": in_progress,
        "completed": completed,
    })
