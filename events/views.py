from django.db.models import Count
from django.http import Http404
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from explore_sthlm_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """ List all events and checks permissions """
    queryset = Event.objects.annotate(
        ratings_count=Count('ratings', distinct=True),
        reviews_count=Count('review', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'ratings__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'ratings_count',
        'reviews_count',
        'ratings__created_at',
    ]
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """ 
    Shows details views of events, also handling error codes.
    Let's you get, edit, and delete events
    """
    queryset = Event.objects.annotate(
        ratings_count=Count('ratings', distinct=True),
        reviews_count=Count('review', distinct=True)
    ).order_by('-created_at')
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]