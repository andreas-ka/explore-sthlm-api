from rest_framework import serializers
from .models import Attend
from django.db import IntegrityError


class AttendSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attend model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attend
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]

    def create(self, validated_data):
        """
        Validation to stop a user posting going to the same event twice
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'It looks like you are already attending this event'
            })
