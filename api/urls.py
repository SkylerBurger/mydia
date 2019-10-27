from django.urls import include, path

# Import serializers


app_name = 'api'
urlpatterns = [
    path('v1/movies/', include('movies.urls')),
    path('v1/shows/', include('shows.urls')),
    path('v1/books/', include('books.urls')),
]