from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from explore_sthlm_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """ List all events and checks permissions """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Shows details views of events, also handling error codes.
    Let's you get, edit, and delete events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]