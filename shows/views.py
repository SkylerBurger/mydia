from rest_framework import generics

from .models import Show
from .serializers import ShowSerializer


class ShowList(generics.ListCreateAPIView):
    """Lists all shows, or create a new show."""
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a show instance."""
    queryset = Show.objects.all()
    serializer_class = ShowSerializer