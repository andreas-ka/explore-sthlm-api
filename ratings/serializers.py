from django.db import IntegrityError
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
        
        
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
