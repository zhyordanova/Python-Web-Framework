from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import PythonCreateForm
from .models import Python
from ..core.decorators import any_group_required
from ..core.mixins import AnyGroupRequireMixin


# def index(request):
#     pythons = Python.objects.all()
#
#     context = {
#         'pythons': pythons,
#         'form': PythonCreateForm(),
#     }
#     return render(request, 'index.html', context)


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    paginate_by = 5


# @login_required(login_url=reverse_lazy('sign-in'))
# @any_group_required(groups=['User'])
# def create(request):
#     if request.method == 'GET':
#         form = PythonCreateForm()
#
#         context = {
#             'form': form,
#         }
#         return render(request, 'create.html', context)
#
#     else:
#         form = PythonCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         context = {
#             'form': form,
#         }
#
#         return render(request, 'create.html', context)


class PythonCreateView(AnyGroupRequireMixin, CreateView):
    template_name = 'create.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('index')
