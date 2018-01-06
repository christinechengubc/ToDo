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

    model = TodoList.objects.all()

    # Number of visits to this view, as counted in the session variable.
    # This is user specific server side stored info discussed in Part 7
    # num_visits=request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={
        	'num_lists':num_lists,
        	'num_items':num_items,
            'object_list':model
#            'num_visits':num_visits
        },
    )

