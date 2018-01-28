from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import TodoItem, TodoList

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_lists=TodoList.objects.all().count()
    num_items=TodoItem.objects.all().count()

    if request.user.is_authenticated():
        the_list = request.user.todolist_set.first()
        todo_list = the_list.todoitem_set.all()
        list_name = the_list.title
    else:
        todo_list = []
        list_name = "No lists available"

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={
        	'num_lists':num_lists,
        	'num_items':num_items,
            'todo_list':todo_list,
            'list_name':list_name
        },
    )

class TodoListView(generic.ListView):
    model = TodoList