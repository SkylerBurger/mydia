from django.db import models
from django.contrib.auth.models import User


class Show(models.Model):
    user = models.ForeignKey(User, related_name='show', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=200)
    season = models.IntegerField('season')
    release_year = models.IntegerField('release year')

    def __str__(self):
        result  = f'{self.user.username} - {self.title}'
        if self.season > 0:
            season = str(self.season).rjust(2, '0')
            result += f' (S{season})'
        return result


class ShowCopy(models.Model):
    show = models.ForeignKey(Show, related_name='copies', on_delete=models.CASCADE)
    platform = models.CharField('platform', max_length=200)
    form = models.CharField('format', max_length=200)

    def __str__(self):
        return f'{self.show.user.username}\'s {self.form} of {self.show.title} on {self.platform}'