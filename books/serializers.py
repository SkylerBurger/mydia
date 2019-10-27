from rest_framework import serializers

from .models import Book, BookCopy


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ['platform', 'form']


class BookSerializer(serializers.ModelSerializer):
    copies = BookCopySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published', 'copies']