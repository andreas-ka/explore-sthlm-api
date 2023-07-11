from rest_framework import generics, permissions
from explore_sthlm_api.permissions import IsOwnerOrReadOnly
from ratings.models import Rating
from ratings.serializers import RatingSerializer


class RatingList(generics.ListCreateAPIView):
    """
    List ratings or create a rating if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a rating or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()