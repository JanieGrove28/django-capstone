from django.urls import path
from . import views

"""
URL configuration for store app.
Maps URLs to views.
"""

urlpatterns = [
    path('', views.home, name='home'),
]
