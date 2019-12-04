"""movieDB3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import movie.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', movie.views.signup, name='signup'),
    path('signout/', movie.views.signout, name='signout'),
    path('signin/', movie.views.signin, name='signin'),
    path('', movie.views.moviehome, name='moviehome'),
    path('detail/<int:pk>', movie.views.detail, name='detail'),
    path('bookmovie/', movie.views.bookmovie, name='bookmovie'),
    path('bookpjh/', movie.views.bookpjh, name='bookpjh'),
    path('bookdate/', movie.views.bookdate, name='bookdate'),
    path('booktime/', movie.views.booktime, name='booktime'),
    path('bookseat/', movie.views.bookseat, name='bookseat'),
    path('ranking/', movie.views.ranking, name='ranking'),
    path('pjhinfo/', movie.views.pjhinfo, name='pjhinfo'),
    path('hello/',  movie.views.hello, name='hello'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
