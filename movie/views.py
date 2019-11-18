

# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

def moviehome(request):
    movie = movieinfo.objects
    return render(request, 'movie/moviehome.html', {'movie' : movie})

def movieSelect(request):
    if request.user.is_authenticated:
        return render(request, 'movie/movieSelect.html')
    else:
        return render(request, 'movie/not_logged_in.html')

def signup(request):
    if request.method == "POST":
        if request.POST["pw"]==request.POST["pwcof"]:
            user = realUser.objects.create_user(
                username=request.POST["id"],
                password=request.POST["pw"],
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname'],
                birth=request.POST['birth'],
                phone=request.POST['phone'],
            )
            auth.login(request, user)
            return redirect('movieSelect')
        return render(request, 'movie/signup.html')
    return render(request, 'movie/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['pw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('movieSelect')
        else:
            return render(request, 'movie/login.html')
    else:
        return render(request, 'movie/login.html')

def signout(request):
    logout(request)
    return redirect('signin')