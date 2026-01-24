from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # <- required for check
from django.contrib import messages
from .forms import RegisterForm

# Registration view using RegisterForm (built on UserCreationForm)
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Invalid information")
    else:
        form = RegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return render(request, "relationship_app/logout.html")

# Home view
def home_view(request):
    return render(request, "relationship_app/home.html")
