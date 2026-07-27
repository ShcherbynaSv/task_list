from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 20


class CreateTaskView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")
    template_name = "tasks/task_form.html"


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect("task-list")


def undo_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return redirect("task-list")


class UpdateTaskView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")
    template_name = "tasks/task_form.html"


class DeleteTaskView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


class TagListView(ListView):
    model = Tag
