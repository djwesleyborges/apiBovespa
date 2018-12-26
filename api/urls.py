from django.contrib import admin
from django.urls import path, include
from api import  views


urlpatterns = [
    path('api/', views.snippet_list),
    path('api/<int:pk>/', views.snippet_detail),
]
