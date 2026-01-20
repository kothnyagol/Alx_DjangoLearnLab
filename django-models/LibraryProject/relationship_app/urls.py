#!/usr/bin/python3
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import LibraryDetailView

urlpatterns = [
    # Function-based view
    path("books/", views.list_books, name="list_books"),

    # Class-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication URLs (ALX REQUIRED)
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
]
