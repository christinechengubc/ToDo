from django.contrib import admin

# Register your models here.

from .models import TodoItem, TodoList, User

admin.site.register(TodoItem)
admin.site.register(TodoList)
admin.site.register(User)
