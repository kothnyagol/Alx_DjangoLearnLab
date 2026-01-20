# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView  # exact import required
from .models import Book
from .models import Library  # exact import required

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
