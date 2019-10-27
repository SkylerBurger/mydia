from django.urls import path

from . import views


app_name = 'books'
urlpatterns = [
    path('', views.BookList.as_view(), name='index'),
    path('<int:pk>/', views.BookDetail.as_view(), name='detail')
]