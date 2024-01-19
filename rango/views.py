from django.shortcuts import render

# Task 3.4
from django.http import HttpResponse

def index(request):
    # Task 4.1
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'creatorname': 'Scott Glidden'}
    return render(request, 'rango/about.html', context=context_dict)