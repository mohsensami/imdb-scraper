from django.urls import path
from . import views


urlpatterns = [
    path('', views.boxOfficeMovies, name='home'),
    path('top250/', views.top250Movies, name='top250'),
] 