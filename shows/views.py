from django.views import generic

from .models import Show


class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'shows_list'

    def get_queryset(self):
        """Return the first five shows."""
        return Show.objects.order_by('title')[:5]


class DetailView(generic.DetailView):
    model = Show
    template_name = 'shows/detail.html'