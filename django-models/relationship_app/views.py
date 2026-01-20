from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from relationship_app!")

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, LibraryProject!")
