from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'users/home.html', {})


def about(request):
    return render(request, 'users/about.html', {})


def register(request):
    return render(request, 'users/register.html', {})


def login(request):
    return render(request, 'users/login.html', {})
