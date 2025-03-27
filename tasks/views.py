from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task

# Display the list of tasks (filtered by user)
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

# Add a new task (assign to the logged-in user)
@login_required
def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            Task.objects.create(title=task_title, user=request.user)
        return redirect('task_list')
    return render(request, 'add_task.html')

# Mark a task as completed (only if the user owns the task)
@login_required
def mark_completed(request, task_id):
    task = Task.objects.filter(id=task_id, user=request.user).first()
    if task:
        task.completed = True
        task.save()
    return redirect('task_list')

# Delete a task (only if the user owns the task)
@login_required
def delete_task(request, task_id):
    task = Task.objects.filter(id=task_id, user=request.user).first()
    if task:
        task.delete()
    return redirect('task_list')
