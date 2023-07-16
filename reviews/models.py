from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Review(models.Model):
    """
    Review model, related to User and Event
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField(blank=False)
    social_media = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.body
