from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils.timezone import now
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
        task_description = request.POST.get('description')  # Capture description
        task_due_date = request.POST.get('due_date')  # Capture due date
        task_priority = request.POST.get('priority')  # Capture priority
        task_category = request.POST.get('category')  # Capture category

        if task_title:  # Ensure title is provided
            Task.objects.create(
                title=task_title,
                description=task_description,
                due_date=task_due_date if task_due_date else None,
                priority=task_priority if task_priority else "M",  # Default to Medium
                category=task_category if task_category else "P",  # Default to Personal
                user=request.user,
                created=now()  # Automatically set the current time
            )
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')  # Correct template path

# Edit an existing task (only if the user owns the task)
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Bind the form with task data
        if form.is_valid():
            form.save()  # Save the updated task details
            return redirect('task_list')  # Redirect to the task list view
    else:
        form = TaskForm(instance=task)  # Pre-fill the form with current task data

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})  # Render the edit form

# Change the status of a task (only if the user owns the task)
@login_required
def change_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user

    if request.method == 'POST':
        new_status = request.POST.get('status')  # Get the new status from the form
        if new_status in ['pending', 'in_progress', 'completed']:  # Validate status
            task.status = new_status  # Update the task's status
            task.save()  # Save changes
        return redirect('task_list')  # Redirect to the task list view

    return render(request, 'tasks/change_status.html', {'task': task})  # Render the status change form


# Mark a task as completed (only if the user owns the task)
@login_required
def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user
    if request.method == 'POST':
        new_status = request.POST.get('status')  # Get the status from the form
        if new_status in ['Pending', 'Completed']:  # Validate the status
            task.status = new_status  # Update the task's status
            task.save()  # Save the changes
    return redirect('task_list')  # Redirect to the task list view


# Delete a task (only if the user owns the task)
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Ensure task belongs to the user
    task.delete()
    return redirect('task_list')

@login_required
def board(request):
    pending_tasks = Task.objects.filter(user=request.user, status='pending')
    in_progress_tasks = Task.objects.filter(user=request.user, status='in_progress')
    completed_tasks = Task.objects.filter(user=request.user, status='completed')
    return render(request, 'tasks/projectboard.html', {
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
    })
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
