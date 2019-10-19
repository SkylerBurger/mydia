from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField('title', max_length=200)
    season = models.IntegerField('season')
    release_year = models.IntegerField('release year')
    platform = models.CharField('platform', max_length=200)
    form = models.CharField('format', max_length=200)

    def __str__(self):
        result  = f'{self.title}'
        if self.season > 0:
            season = str(self.season).rjust(2, '0')
            result += f' (S{season})'
        return result