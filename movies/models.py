from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField('title', max_length=200)
    release_year = models.IntegerField('release year')
    mpaa_rating = models.CharField('MPAA rating', max_length=5)
    run_time = models.IntegerField('run time')

    def __str__(self):
        return f'{self.title} ({self.release_year})'


class MovieCopy(models.Model):
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)
    platform = models.CharField('platform', max_length=200)
    form = models.CharField('format', max_length=200)

    def __str__(self):
        return f'{self.form} of {self.film} on {self.platform}'