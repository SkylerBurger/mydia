from django.views import generic

from .models import Show
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, this is the shows page.")

class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'shows_list'

    def get_queryset(self):
        """Return the first five movies."""
        return Show.objects.order_by('title')[:5]

class DetailView(generic.DetailView):
    model = Show
    template_name = 'shows/detail.html'