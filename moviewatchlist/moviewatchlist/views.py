from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Register  # Make sure to import the Pet model

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def movies(request):
    return render(request, 'blog.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def registerUser(request):
    if request.method == "POST":
        saverecord = Register()
        saverecord.name = request.POST.get('name')
        saverecord.email = request.POST.get('email')
        saverecord.contact_number = request.POST.get('contact_number')
        saverecord.password = request.POST.get('password')  # this password is not working
        saverecord.save()
        messages.success(request, 'User Registered')
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')