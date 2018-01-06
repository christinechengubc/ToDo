from django.contrib import admin

# Register your models here.

from .models import TodoItem, TodoList, Profile, User

admin.site.register(TodoItem)
admin.site.register(TodoList)
admin.site.register(Profile)
