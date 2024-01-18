from django.shortcuts import render

# Task 3.4
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")