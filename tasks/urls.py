from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("task_list/", views.task_list, name="task_list"),
    path("add-task/", views.add_task, name="add_task"),
    path("board/", views.board, name="board"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path(
        "mark_completed/<int:task_id>/",
        views.mark_completed,
        name="mark_completed",
    ),
    path("update-task-status/<int:task_id>/", views.update_task_status, name="update_task_status"),
    path("edit-task/<int:task_id>/", views.edit_task, name="edit_task"),
]
