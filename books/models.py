from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('title', max_length=200)
    author = models.CharField('author(s)', max_length=200)
    published = models.IntegerField('published')
    platform = models.CharField('platform', max_length=200)
    form = models.CharField('format', max_length=200)

    def __str__(self):
        return f'{self.title} by {self.author}'