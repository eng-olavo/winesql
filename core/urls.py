from django.shortcuts import render
from django.urls import path
from .views import index


urlpatterns = [
    path('', index, name='index'),
]