from django.urls import path

from . import views


app_name = 'shows'
urlpatterns = [
    path('', views.ShowList.as_view(), name='index'),
    path('<int:pk>/', views.ShowDetail.as_view(), name='detail')
]