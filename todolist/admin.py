from django.contrib import admin
from . models import TodoList, Task


@admin.register(TodoList)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'todolist', 'due_time', 'priority', 'status']
    list_editable = ['due_time', 'priority', 'status']
