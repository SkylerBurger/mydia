from rest_framework import generics

from .models import Movie
from .serializers import MovieSerializer


class MovieList(generics.ListCreateAPIView):
    """ Lists all movies, or create a new movie."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update, or delete a movie instance."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer