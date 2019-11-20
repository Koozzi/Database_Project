

# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

def realinfo(request):
    return render(request, 'movie/realinfo.html')

def actorinfo(request):
    return render(request, 'movie/actorinfo.html')

def directorinfo(request):
    return render(request, 'movie/directorinfo.html')

def moviehome(request):
    if request.user.is_authenticated:
        movie = movieinfo.objects.filter(movie_playing =1)
        movie1 = movieinfo.objects.filter(movie_playing=2)
        return render(request, 'movie/moviehome.html', {
            'movie' : movie,
            'movie1' : movie1,
        })
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
            return redirect('moviehome')
        return render(request, 'movie/signup.html')
    return render(request, 'movie/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['id']
        password = request.POST['pw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('moviehome')
        else:
            return render(request, 'movie/login.html')
    else:
        return render(request, 'movie/login.html')

def signout(request):
    logout(request)
    return redirect('signin')

def detail(request, pk):
    moviedetail = get_object_or_404(movieinfo, pk=pk)
    return render(request, 'movie/detail.html', {
        'moviedetail':moviedetail
    })