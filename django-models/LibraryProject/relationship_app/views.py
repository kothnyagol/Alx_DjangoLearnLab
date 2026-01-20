#!/usr/bin/python3
# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library  # <-- This exact import is required

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
