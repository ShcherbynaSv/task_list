"""
URL configuration for task_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from tasks.views import (
    TaskListView,
    CreateTaskView,
    complete_task,
    undo_task,
    UpdateTaskView,
    DeleteTaskView,
    TagListView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", CreateTaskView.as_view(), name="create-task"),
    path("tasks/<int:pk>/complete/", complete_task, name="complete-task"),
    path("tasks/<int:pk>/undo/", undo_task, name="undo-task"),
    path("tasks/<int:pk>/update/", UpdateTaskView.as_view(), name="update-task"),
    path("tasks/<int:pk>/delete/", DeleteTaskView.as_view(), name="delete-task"),
    path("", TagListView.as_view(), name="tag-list"),
]
