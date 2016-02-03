from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
# Import the Category model
from rango.models import Category,Page


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    category_list = Category.objects.order_by('-likes')[:5]

    # Construct a dictionary to pass to the template engine as its context.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    context_dict = {'categories':category_list}

    # Render the response and send it back!
    return render(request,'rango/index.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context_dict )

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category = category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages

        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict )
