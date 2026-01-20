#!/usr/bin/python3
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpResponse

# ✅ REQUIRED ALX IMPORTS (VERY IMPORTANT)
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Book, Library


# -----------------------------
# FUNCTION-BASED VIEW
# -----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# -----------------------------
# CLASS-BASED VIEW
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"


# -----------------------------
# AUTHENTICATION VIEWS
# -----------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ REQUIRED BY ALX
            return redirect("list_books")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("list_books")

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("login")
