from django.shortcuts import render, redirect

from .forms import PythonCreateForm
from .models import Python


def index(request):
    pythons = Python.objects.all()

    context = {
        'pythons': pythons,
        'form': PythonCreateForm(),
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()

        context = {
            'form': form,
        }
        return render(request, 'create.html', context)

    else:
        form = PythonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

