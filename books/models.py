from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, related_name='book', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=200)
    author = models.CharField('author(s)', max_length=200)
    published = models.IntegerField('published')

    def __str__(self):
        return f'{self.user.username} - {self.title} by {self.author}'


class BookCopy(models.Model):
    book = models.ForeignKey(Book, related_name='copies', on_delete=models.CASCADE)
    platform = models.CharField('platform', max_length=200)
    form = models.CharField('format', max_length=200)

    def __str__(self):
        return f'{self.book.user.username}\'s {self.form} of {self.book.title} on {self.platform}'