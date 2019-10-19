from django.views import generic

from .models import Book


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books_list'

    def get_queryset(self):
        """Return the first five books."""
        return Book.objects.order_by('title')[:5]


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'