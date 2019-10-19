from django.views import generic

from .models import Movie


class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'movies_list'

    def get_queryset(self):
        """Return the first five movies."""
        return Movie.objects.order_by('title')[:5]


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'