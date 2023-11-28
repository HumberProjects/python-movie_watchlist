from django.shortcuts import render

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

