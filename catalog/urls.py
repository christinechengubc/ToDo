from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todo_list$', views.TodoListView.as_view(), name='todo_list'),
]