from rest_framework import generics, permissions
from explore_sthlm_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class FollowerDetailList(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]