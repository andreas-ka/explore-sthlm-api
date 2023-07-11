from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the ratings model.
    """
    
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Rating
        fields = ['id', 'owner', 'rating', 'event', 'created_at']