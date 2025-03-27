from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


# Display the list of tasks (filtered by user)
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Restrict to the logged-in user's tasks
    # return render(request, 'tasks/task_list.html', {'tasks': tasks})

    form = TaskForm()
    return render(request, 'tasks/task_list.html', {'form': form, 'tasks': tasks})


# Add a new task (assign to the logged-in user)
@login_required
def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            Task.objects.create(title=task_title, user=request.user)  # Ensure task is linked to the user
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')  # Correct template path


# Mark a task as completed (only if the user owns the task)
@login_required
def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user
    task.completed = True
    task.save()
    return redirect('task_list')


# Delete a task (only if the user owns the task)
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user
    task.delete()
    return redirect('task_list')


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
    # tasks = Task.objects.filter(user=request.user)
    tasks = Task.objects.filter(user=request.user).order_by('due_date')  # Restrict tasks to the logged-in user
    pending = tasks.filter(status="P")
    in_progress = tasks.filter(status="IP")
    completed = tasks.filter(status="C")

    return render(request, "tasks/projectboard.html", {
        "pending": pending,
        "in_progress": in_progress,
        "completed": completed,
    })


def home(request):
    return render(request, 'tasks/home.html')
