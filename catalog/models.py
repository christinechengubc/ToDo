from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    todo_list = models.ForeignKey('TodoList', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('todo-detail', args=[str(self.id)])

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    users = models.ManyToManyField(User, help_text="Share this list with another user...")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todolist-items', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dummy_attrib = models.CharField(max_length=100, null=True, blank = True)

    # def __str__(self):
    #     return self.user.get_username

    # def get_absolute_url(self):
    #     return reverse('user-detail', args=[str(self.id)])

# # Update profile class whenever its user class is updated
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
