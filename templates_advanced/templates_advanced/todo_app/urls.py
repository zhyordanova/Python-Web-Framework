from django.urls import path

from templates_advanced.todo_app.views import list_todos, create_todo

urlpatterns = [
    path('', list_todos, name='list todos'),
    path('create/', create_todo, name='create todo'),
]
