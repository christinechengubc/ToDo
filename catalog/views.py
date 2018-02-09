from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

from .models import TodoItem, TodoList
from .forms import AddItemForm

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_lists=TodoList.objects.all().count()
    num_items=TodoItem.objects.all().count()

    if request.user.is_authenticated:
        the_list = request.user.todolist_set.first()
        todo_list = the_list.todoitem_set.all()
        list_name = the_list.title
        user_lists = request.user.todolist_set.all()
    else:
        todo_list = []
        list_name = "No lists available"

    if request.method == 'POST':
        form = AddItemForm(user_lists, list_name, request.POST)

        if form.is_valid():
            item_title = form.cleaned_data['item_title']
            item_list = form.cleaned_data['item_list']
            chosen_list = TodoList.objects.filter(users = request.user, title = item_list).first()
            TodoItem.objects.create(title = item_title, user = request.user, todo_list = chosen_list)

            return HttpResponseRedirect(reverse('index'));

    else:
        print(user_lists)
        form = AddItemForm(user_lists, list_name)

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={
        	'num_lists':num_lists,
        	'num_items':num_items,
            'todo_list':todo_list,
            'list_name':list_name,
            'form': form
        },
    )

class TodoListView(generic.ListView):
    model = TodoList
