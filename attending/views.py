from rest_framework import generics, permissions
from explore_sthlm_api.permissions import IsOwnerOrReadOnly
from attending.models import Attend
from attending.serializers import AttendSerializer


class AttendList(generics.ListCreateAPIView):
    """
    List attending posts or create a attend post if logged in
    The perform_create method associates the attend post with the logged
    in user.
    """
    serializer_class = AttendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Attend.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendDetailList(generics.RetrieveDestroyAPIView):
    """
    Retrieve a attend post, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendSerializer
    queryset = Attend.objects.all()
