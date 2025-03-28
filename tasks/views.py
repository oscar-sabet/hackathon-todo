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
