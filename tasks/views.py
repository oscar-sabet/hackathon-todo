from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils.timezone import now
from .forms import TaskForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Display the list of tasks (filtered by user)
@login_required
def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.status = 'pending'  # Default status for new tasks
            task.save()
            return redirect('task_list')

    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    return render(request, 'tasks/task_list.html', {'form': form, 'tasks': tasks})


# Add a new task (assign to the logged-in user)
@csrf_exempt
@login_required
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', 'New Task')
        status = data.get('status', 'pending')
        task = Task.objects.create(title=title, status=status, user=request.user)
        return JsonResponse({'success': True, 'task_id': task.id})
    return JsonResponse({'success': False}, status=400)

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
        new_status = request.POST.get('status') 
        print(new_status)
        # Get the status from the form
        if new_status in ['pending', 'completed']:  # Validate the status
            task.status = new_status  # Update the task's status
            print(" task status updated", task.status)
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


def home(request):
    return render(request, 'tasks/home.html')


@csrf_exempt
@login_required
def update_task_status(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_status = data.get('status')
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.status = new_status
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
