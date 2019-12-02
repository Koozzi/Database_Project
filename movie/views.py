

# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .forms import *
from django.db.models import Avg

def moviehome(request):
    # if request.user.is_authenticated:
        movie = movieinfo.objects.filter(movie_playing =1)
        movie1 = movieinfo.objects.filter(movie_playing=2)
        return render(request, 'movie/moviehome.html', {
            'movie' : movie,
            'movie1' : movie1,
            'user' : request.user,
        })
    # else:
    #     return render(request, 'movie/not_logged_in.html')

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
    pjh_id = request.GET.get('pjh')
    date = request.GET.get('date')
    movie_message = "{}".format(movie)#movie_message 에는 고객이 선택한 영화 고유 id가 들어있다.
    pjh_message = "{}".format(pjh_id)#pjh_message 에는 고객이 선택한 지점 고유 id가 들어있다.
    date_message = "{}".format(date)#date_message 에는 고객이 선택한 날짜가 들어있다.
    movie_selected = movieinfo.objects.filter(movie_id = movie_message)
    pjh_selected = pjh.objects.filter(pjh_id = pjh_message)
    timetables = timetable.objects.select_related("movie_name").filter(movie_name=movie_message, pjh_id=pjh_message, date=date_message)
    context={
        'movie_message': movie_message,
        'pjh_message': pjh_message,
        'date_message': date_message,
        'timetables': timetables,
        'movie_selected': movie_selected,
        "pjh_selected": pjh_selected,
    }
    return render(request, 'movie/book_time.html', context)

def bookseat(request):
    movie = request.GET.get('movie')
    pjh = request.GET.get('pjh')
    date = request.GET.get('date')
    time = request.GET.get('time')
    movie_message = "{}".format(movie)  #movie_message 에는 고객이 선택한 영화 고유 id가 들어있다.
    pjh_message = "{}".format(pjh)      #pjh_message 에는 고객이 선택한 지점 고유 id가 들어있다.
    date_message = "{}".format(date)    #date_message 에는 고객이 선택한 날짜가 들어있다.
    time_message = "{}".format(time)    #time_message 에는 고객이 선택한 시간이 들어있다.
    booked_seats = booking.objects.filter(movie=movie_message,
                                          pjh=pjh_message,
                                          date=date_message,
                                          time=time_message,
                                          refund=0)
    rowA = []
    not_booked_seats_rowA = seat.objects.filter(seat_row='A')
    for i in range(len(not_booked_seats_rowA)):
        rowA.append(not_booked_seats_rowA[i])

    for i in range(len(not_booked_seats_rowA)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowA[i].seat_num == booked_seats[j].seat:
                rowA[i] = "X"
    rowB=[]
    not_booked_seats_rowB = seat.objects.filter(seat_row='B')
    for i in range(len(not_booked_seats_rowB)):
        rowB.append(not_booked_seats_rowB[i])

    for i in range(len(not_booked_seats_rowB)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowB[i].seat_num == booked_seats[j].seat:
                rowB[i] = "X"

    rowC=[]
    not_booked_seats_rowC = seat.objects.filter(seat_row='C')
    for i in range(len(not_booked_seats_rowC)):
        rowC.append(not_booked_seats_rowC[i])

    for i in range(len(not_booked_seats_rowC)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowC[i].seat_num == booked_seats[j].seat:
                rowC[i] = "X"
    rowD=[]
    not_booked_seats_rowD = seat.objects.filter(seat_row='D')
    for i in range(len(not_booked_seats_rowD)):
        rowD.append(not_booked_seats_rowD[i])

    for i in range(len(not_booked_seats_rowD)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowD[i].seat_num == booked_seats[j].seat:
                rowD[i] = "X"

    rowE=[]
    not_booked_seats_rowE = seat.objects.filter(seat_row='E')
    for i in range(len(not_booked_seats_rowE)):
        rowE.append(not_booked_seats_rowE[i])

    for i in range(len(not_booked_seats_rowE)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowE[i].seat_num == booked_seats[j].seat:
                rowE[i] = "X"

    rowF=[]
    not_booked_seats_rowF = seat.objects.filter(seat_row='F')
    for i in range(len(not_booked_seats_rowF)):
        rowF.append(not_booked_seats_rowF[i])

    for i in range(len(not_booked_seats_rowF)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowF[i].seat_num == booked_seats[j].seat:
                rowF[i] = "X"

    rowG=[]
    not_booked_seats_rowG = seat.objects.filter(seat_row='G')
    for i in range(len(not_booked_seats_rowG)):
        rowG.append(not_booked_seats_rowG[i])

    for i in range(len(not_booked_seats_rowG)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowG[i].seat_num == booked_seats[j].seat:
                rowG[i] = "X"

    rowH=[]
    not_booked_seats_rowH = seat.objects.filter(seat_row='H')
    for i in range(len(not_booked_seats_rowH)):
        rowH.append(not_booked_seats_rowH[i])

    for i in range(len(not_booked_seats_rowH)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowH[i].seat_num == booked_seats[j].seat:
                rowH[i] = "X"

    rowI=[]
    not_booked_seats_rowI = seat.objects.filter(seat_row='I')
    for i in range(len(not_booked_seats_rowI)):
        rowI.append(not_booked_seats_rowI[i])

    for i in range(len(not_booked_seats_rowI)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowI[i].seat_num == booked_seats[j].seat:
                rowI[i] = "X"

    rowJ=[]
    not_booked_seats_rowJ = seat.objects.filter(seat_row='J')
    for i in range(len(not_booked_seats_rowJ)):
        rowJ.append(not_booked_seats_rowJ[i])

    for i in range(len(not_booked_seats_rowJ)):
        for j in range(len(booked_seats)):
            if not_booked_seats_rowJ[i].seat_num == booked_seats[j].seat:
                rowJ[i] = "X"

    context={
        'movie_message': movie_message,
        'pjh_message': pjh_message,
        'date_message': date_message,
        'time_message': time_message,
        'booked_seats': booked_seats,
        'not_booked_seats_rowA': not_booked_seats_rowA,
        'not_booked_seats_rowB': not_booked_seats_rowB,
        'not_booked_seats_rowC': not_booked_seats_rowC,
        'not_booked_seats_rowD': not_booked_seats_rowD,
        'not_booked_seats_rowE': not_booked_seats_rowE,
        'not_booked_seats_rowF': not_booked_seats_rowF,
        'not_booked_seats_rowG': not_booked_seats_rowG,
        'not_booked_seats_rowH': not_booked_seats_rowH,
        'not_booked_seats_rowI': not_booked_seats_rowI,
        'not_booked_seats_rowJ': not_booked_seats_rowJ,
        'rowA': rowA,
        'rowB': rowB,
        'rowC': rowC,
        'rowD': rowD,
        'rowE': rowE,
        'rowF': rowF,
        'rowG': rowG,
        'rowH': rowH,
        'rowI': rowI,
        'rowJ': rowJ,
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
    return redirect('moviehome')

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

    reviews = review.objects.select_related("movie_id").filter(movie_id=pk)
    avg = review.objects.filter(movie_id=pk).aggregate(Avg('review_grade'))

    score = []
    score.append(avg['review_grade__avg'])

    score_update = movieinfo.objects.get(movie_id=pk)
    score_update.movie_score = score[0]
    score_update.save()
    return render(request, 'movie/detail.html', {
        'moviedetail': moviedetail,
        'reviews': reviews,
        'id': id,
        'form':form,
        'user':request.user,
        'score': score,
    })


def ranking(request):
    movies = movieinfo.objects.all().exclude(movie_score = None).order_by('-movie_score')
    return render(request, 'movie/ranking.html', {
        'movies':movies,
    })

def pjhinfo(request):
    pjhs = pjh.objects.all()
    return render(request, 'movie/pjhinfo.html', {
        'pjhs': pjhs
    })