from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from explore_sthlm_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer


class ReviewList(generics.ListCreateAPIView):
    """
    List reviews and add reviews if logged in
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'event'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete reviews if you are the owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
