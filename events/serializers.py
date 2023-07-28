from rest_framework import serializers
from .models import Event
from ratings.models import Rating
from attending.models import Attend
from reviews.models import Review


class EventSerializer(serializers.ModelSerializer):
    """
    Event serializer with counts and average
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    rating_id = serializers.SerializerMethodField()
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    ratings_count = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    attend_id = serializers.SerializerMethodField()
    attend_count = serializers.ReadOnlyField()
    rating_average = serializers.SerializerMethodField()
    rating = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Sorry the image size cant be larger than 2mb!'
                )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Sorry the image height can not be larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Sorry the image width can not be larger than 4096px!'
            )
        return value
    
    def get_rating_average(self, obj):
        # Calculate the average rating
        ratings = obj.ratings.all()
        count = ratings.count()
        if count > 0:
            total_sum = sum(rating.rating for rating in ratings)
            return total_sum / count
        return None

    def get_ratings_count(self, obj):
        # Get the count of ratings
        return obj.ratings.count()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                owner=user, event=obj
            ).first()
            return rating.id if rating else None
        return None
    
    def get_attend_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attend = Attend.objects.filter(
                owner=user, event=obj
            ).first()
            return attend.id if attend else None
        return None
    

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'description', 'image', 'start_date',
            'end_date', 'category', 'event_location', 'cost', 'rating_id',
            'ratings_count', 'comments_count', 'attend_count',
            'rating_average', 'attend_id', 'rating',
        ]