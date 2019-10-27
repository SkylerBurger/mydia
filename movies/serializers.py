from rest_framework import serializers

from .models import Movie, MovieCopy


class MovieCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCopy
        fields = ['platform', 'form']


class MovieSerializer(serializers.ModelSerializer):
    copies = MovieCopySerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'mpaa_rating', 'run_time', 'copies']