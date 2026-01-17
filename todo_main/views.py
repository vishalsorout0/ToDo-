from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by("-modified_at")#if we use - it will be in descending order otherwise it will be in ascending order
    context={
        'tasks':tasks,
    }
    return render(request,"home.html",context)
