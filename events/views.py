from django.db.models import Count, Avg
from django.http import Http404
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Event
from ratings.models import Rating
from attending.models import Attend
from .serializers import EventSerializer
from explore_sthlm_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """ List all events and checks permissions
    rating_average is not used now, will be a better option
    in future then current one. Thats why i kept it.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Event.objects.annotate(
        ratings_count=Count('ratings', distinct=True),
        comments_count=Count('comment', distinct=True),
        attend_count=Count('attend', distinct=True),
        rating_average=Avg('ratings__rating', distinct=True),
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
        'category',
        'attend__owner__profile',
        'start_date',
    ]
    search_fields = [
        'owner__username',
        'title',
        'start_date'
    ]
    ordering_fields = [
        'comments_count',
        'attend_count',
        'ratings__created_at',
        'rating_average',
    ]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Shows details views of events, also handling error codes.
    Let's you get, edit, and delete events
    """
    queryset = Event.objects.annotate(
        ratings_count=Count('ratings', distinct=True),
        comments_count=Count('comment', distinct=True),
        attend_count=Count('attend', distinct=True),
        rating_average=Avg('ratings__rating', distinct=True),
    ).order_by('-created_at')
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
