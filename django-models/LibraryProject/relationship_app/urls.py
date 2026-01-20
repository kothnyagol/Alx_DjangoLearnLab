from django.urls import path
from .views import register_view, CustomLoginView, CustomLogoutView, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
