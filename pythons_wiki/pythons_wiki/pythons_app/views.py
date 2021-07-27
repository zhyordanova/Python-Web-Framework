from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import PythonCreateForm
from .models import Python
from ..core.decorators import any_group_required


def sign_in(request):
    user = authenticate(username='alex', password='123PqweD')
    login(request, user)
    return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')


def index(request):
    pythons = Python.objects.all()

    context = {
        'pythons': pythons,
        'form': PythonCreateForm(),
    }
    return render(request, 'index.html', context)


# @login_required(login_url=reverse_lazy('sign-in'))
@any_group_required(groups=['User'])
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
