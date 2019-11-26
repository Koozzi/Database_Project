

# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .forms import *

def moviehome(request):
    if request.user.is_authenticated:
        movie = movieinfo.objects.filter(movie_playing =1)
        movie1 = movieinfo.objects.filter(movie_playing=2)
        return render(request, 'movie/moviehome.html', {
            'movie' : movie,
            'movie1' : movie1,
            'user' : request.user,
        })
    else:
        return render(request, 'movie/not_logged_in.html')

def bookmovie(request):
    current_movie = movieinfo.objects.filter(movie_playing=1)
    return render(request, 'movie/book_movie.html', {
        'current_movie':current_movie,
    })

def bookpjh(request):
    movie = request.GET.get('movie')
    movie_message = "{}".format(movie) #movie_message 에는 고객이 선택한 영화 고유 id가 들어있다.
    pjhs = pjh.objects.all()
    context = {
        'pjhs': pjhs,
        'movie_message': movie_message,
    }
    return render(request, 'movie/book_pjh.html',context)

def bookdate(request):
    movie = request.GET.get('movie')
    pjh = request.GET.get('pjh')
    movie_message = "{}".format(movie)#movie_message 에는 고객이 선택한 영화 고유 id가 들어있다.
    pjh_message = "{}".format(pjh)#pjh_message 에는 고객이 선택한 지점 고유 id가 들어있다.
    context={
        'movie_message': movie_message,
        'pjh_message': pjh_message,
    }
    return render(request,  'movie/book_date.html', context)

def booktime(request):
    movie = request.GET.get('movie')
    pjh = request.GET.get('pjh')
    date = request.GET.get('date')
    movie_message = "{}".format(movie)#movie_message 에는 고객이 선택한 영화 고유 id가 들어있다.
    pjh_message = "{}".format(pjh)#pjh_message 에는 고객이 선택한 지점 고유 id가 들어있다.
    date_message = "{}".format(date)#date_message 에는 고객이 선택한 날짜가 들어있다.
    time = timetable.objects.select_related("movie_name").filter(movie_name=movie_message, pjh_id=pjh_message, date=date_message)
    context={
        'movie_message': movie_message,
        'pjh_message': pjh_message,
        'date_message': date_message,
        'time': time,
    }
    return render(request, 'movie/book_time.html', context)

def bookseat(request):
    movie = request.GET.get('movie')
    pjh = request.GET.get('pjh')
    date = request.GET.get('date')
    seat = request.GET.get('seat')
    movie_message = "{}".format(movie)#movie_message 에는 고객이 선택한 영화 고유 id가 들어있다.
    pjh_message = "{}".format(pjh)#pjh_message 에는 고객이 선택한 지점 고유 id가 들어있다.
    date_message = "{}".format(date)#date_message 에는 고객이 선택한 날짜가 들어있다.
    seat_message = "{}".format(seat)#seat_message 에는 고객이 선택한 자리가 들어있다.

    context={
        'movie_message': movie_message,
        'pjh_message': pjh_message,
        'date_message': date_message,
        'seat_message': seat_message,
    }
    return render(request, 'movie/book_seat.html', context)

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
    if request.method == "POST":
        form = reviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.username = request.user
            comment.movie_id = moviedetail
            comment.save()
            return redirect('detail', pk = pk)
    else:
        form = reviewForm()
    movie = request.GET.get('id')
    movie_message = "{}".format(movie)
    reviews = review.objects.select_related("movie_id").filter(movie_id=pk)
    return render(request, 'movie/detail.html', {
        'moviedetail': moviedetail,
        'reviews': reviews,
        'id': id,
        'form':form,
        'user':request.user,
    })