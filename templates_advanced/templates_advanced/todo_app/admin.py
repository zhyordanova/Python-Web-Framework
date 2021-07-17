from django.contrib import admin

from templates_advanced.todo_app.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

