from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Register  # Make sure to import the Pet model
from .models import AddCategory, AddMovie 

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

def loginUser(request):
    if request.method == "POST":
        loginuser = Login()
        loginuser.email = request.POST.get('email')
        

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
    
def addNewCategory(request):
    if request.method == "POST":
        saverecord = AddCategory()
        saverecord.category_name = request.POST.get('category_name')
        saverecord.description = request.POST.get('description')       
        saverecord.save()
        messages.success(request, 'Category Added Registered')
        return render(request, 'index.html')
    else:
        return render(request, 'category.html')
    
def addNewMovie(request):
    if request.method == "POST":
        saverecord = AddMovie()
        saverecord.title = request.POST.get('title')
        saverecord.release_year = request.POST.get('release_year') 
        saverecord.director = request.POST.get('director')
        saverecord.category_id = request.POST.get('category_id')       
        saverecord.summary = request.POST.get('summary')
        saverecord.rating = request.POST.get('rating') 
        saverecord.save()
        messages.success(request, 'Movie Added to the Movie list')
        return render(request, 'index.html')
    else:
        return render(request, 'add_movie.html')