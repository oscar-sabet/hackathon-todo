from django.urls import path
from . import views

urlpatterns = [
    path("task_list/", views.task_list, name="task_list"),
    path("add_task/", views.add_task, name="add_task"),
    path("board/", views.board, name="board"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path(
        "mark_completed/<int:task_id>/",
        views.mark_completed,
        name="mark_completed",
    ),
    path("index/", views.index, name="index"),
]
