from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    """Lists all books, or create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a book instance."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer