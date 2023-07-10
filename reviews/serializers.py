from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """ 
    Serializer for the Review model,
    Also adds 3 more fields to it.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    """ Serializing the Review model  """
    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'review',
            'body', 'is_owner', 'social_media', 
            'profile_image', 'profile_id',
        ]
        
class ReviewDetailSerializer(ReviewSerializer):
    """ 
    Serializer for Review but in detail view 
    """
    review = serializers.ReadOnlyField(source='event.id')