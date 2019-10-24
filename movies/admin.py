from django.contrib import admin
from .models import Movie, MovieCopy

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieCopy)