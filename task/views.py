from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout as auth_logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from task.models import Task
from task.forms import TaskForm, CustomUserProfile

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        # Get tasks belonging to the logged-in user
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = None

    context = {
        'tasks': tasks,
        'task_count': tasks.count() if tasks else 0  # count tasks
    }
    return render(request, 'task/index.html', context)


@login_required
def tasks(request):
    """Show all tasks and their decriptions."""
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'tasks':tasks,
    }

    return render(request, 'task/tasks.html', context)
@login_required
def task(request, task_id):
    """Show a single task and its details."""
    task = Task.objects.get(id=task_id, user=request.user)
    context = {
        'task':task,
    }

    return render(request, 'task/task.html', context)

@login_required
def add_task(request):
    if request.method != 'POST':
        form = TaskForm()

    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
        return redirect('task:tasks')
    
    context = {
        'form':form,
    }

    return render(request, 'task/add_task.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task:tasks')

    return render(request, 'task/delete_task.html', {'task': task})

@login_required
def logout(request):
    """Log the user out."""
    auth_logout(request)

    return redirect('task:index')

    

from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = CustomUserProfile(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)  # 🔥 no authenticate needed
            messages.success(request, 'Signed up successfully.')
            return redirect('task:index')

    else:
        form = CustomUserProfile()

    return render(request, 'task/register.html', {'form': form})



@login_required
def update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # only allow owner

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:tasks')  # redirect to task list
    else:
        form = TaskForm(instance=task)  # populate form with existing data

    context = {
        'form': form,
        'task': task
    }

    return render(request, 'task/update.html', context)


def toggle(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()

    return redirect('task:task', task_id=task.id)











        


