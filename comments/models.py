from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Comment(models.Model):
    """
    Comment model, related to Event
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content