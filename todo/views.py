from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

def addtask(request):
    task_data=request.POST['task']
    Task.objects.create(task=task_data)
    return redirect('home')
# Create your views here.
