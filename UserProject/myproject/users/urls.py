from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login')
]