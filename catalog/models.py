from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the task")
    todo_list = models.ForeignKey('TodoList', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('todo-detail', args=[str(self.id)])

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    users = models.ManyToManyField('User', help_text="Share this list with another user...")
    todo_items = models.ManyToManyField(TodoItem)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todolist-items', args=[str(self.id)])

class User(models.Model):
    username = models.CharField(max_length=20)
    todo_lists = models.ManyToManyField(TodoList)

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse('user-detail', args=[str(self.id)])
