from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from cats.cats_app.common.form_mixins import BootStrapFormViewMixin
from cats.cats_app.models import Cat


def index(request):
    context = {
        'title': 'Hello from FunctionBaseView!',
    }
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hello from ClassBaseView!',
        }


def show_cats(request):
    context = {
        'cats': Cat.objects.all(),
        'cats_title': 'Hello from FunctionBaseView Cats!',
    }

    return render(request, 'cats-list.html', context)


class CatCreateView(BootStrapFormViewMixin, CreateView):
    model = Cat
    fields = '__all__'
    template_name = 'create-cat.html'
    success_url = reverse_lazy('cbv show cats')


class ShowCatsView(ListView):
    model = Cat
    template_name = 'cats-list.html'
    context_object_name = 'cats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats_title'] = 'Hello from ClassBaseView Cats!'
        return context



