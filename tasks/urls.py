from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('tasks', views.task_list, name='task_list'),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),

]
