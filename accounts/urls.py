from tkinter import N
from unicodedata import name
from unittest.mock import patch
from django.urls import path
from .views import SignUpView , ProfileView , ChangeView, UserDeleteView

urlpatterns = [
    path('signup/' , SignUpView.as_view() , name='signup'),
    path('profile/<int:pk>' , ProfileView.as_view() , name='profile'),
    path('change/<int:pk>' , ChangeView.as_view() , name='change'),
    path('delete/<int:pk>' , UserDeleteView.as_view() , name='delete')
]