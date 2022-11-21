from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'GlavApp/index.html', {'title': 'Главная стр', 'tasks': tasks})


def about(request):
    return render(request, 'GlavApp/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Неправильно'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'GlavApp/create.html', context)


