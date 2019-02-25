from django.urls import path
from .views import render_employees

urlpatterns = [
    path('', render_employees)
]