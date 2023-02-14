from django.urls import path
from . import views


urlpatterns = [
    path('', views.boxOfficeMovies, name='home'),
    path('top250/', views.top250Movies, name='top250'),
    path('box-office-all/', views.boxOfficeAllMovies, name='boxall'),
    path('comming-soon/', views.commingSoonMovies, name='commingsoon'),
    path('in-theaters/', views.inTheaters, name='in-theaters'),
    path('popular-movies/', views.popularMovies, name='popularmovies'),
] 