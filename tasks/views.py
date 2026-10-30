from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Task

def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    tasks = Task.objects.order_by("-created")
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def toggle_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.done = not task.done
        task.save()
    return redirect("task_list")
