#!/usr/bin/python3
from django.shortcuts import render, redirect
from django.views.generic import DetailView

# ✅ ALX-REQUIRED AUTH IMPORTS
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Book, Library


# -------------------------------------------------
# FUNCTION-BASED VIEW
# -------------------------------------------------
def list_books(request):
    """
    Lists all books in the database.
    Displays book title and author.
    """
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# -------------------------------------------------
# CLASS-BASED VIEW
# -------------------------------------------------
class LibraryDetailView(DetailView):
    """
    Displays details of a specific library
    and lists all books in that library.
    """
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"


# -------------------------------------------------
# AUTHENTICATION VIEWS
# -------------------------------------------------
def register(request):
    """
    Handles user registration using
    Django's built-in UserCreationForm.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ REQUIRED BY ALX
            return redirect("list_books")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})
