from rest_framework import serializers

from .models import Movie, MovieCopy


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'mpaa_rating', 'run_time']


class MovieCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCopy
        fields = ['movie', 'platform', 'form']