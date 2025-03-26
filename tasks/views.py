from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def tasks(request):
    return HttpResponse("Hello, DoodleTo tasks!")


def board(request):
    
    order_by = request.GET.get("order_by", "created")
    tasks = Task.objects.order_by(order_by)
    pending = tasks.filter(status="P")
    in_progress = tasks.filter(status="IP")
    completed = tasks.filter(status="C")
    
    return render(request, "** insert template **", {
        "pending": pending,
        "in_progress": in_progress,
        "completed": completed,
    })