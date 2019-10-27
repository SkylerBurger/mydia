from django.urls import path

from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.MovieList.as_view(), name='index'),
    path('<int:pk>', views.MovieDetail.as_view(), name='detail')
]