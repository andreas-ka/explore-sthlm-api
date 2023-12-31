from django.db import models
from django.contrib.auth.models import User
from datetime import date

EVENT_CATEGORIES = (
    ("Sport", "Sport"),
    ("Music", "Music"),
    ("Culture", "Culture"),
    ("Family", "Family"),
    ("Food", "Food"),
    ("Shopping", "Shopping"),
    ("Sightseeing", "Sightseeing"),
)

class Event(models.Model):
    """
    Event model, related to 'owner'.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    category = models.CharField(
        max_length=255, blank=False, choices=EVENT_CATEGORIES, default='Sightseeing'
        )
    event_location = models.CharField(max_length=255, blank=False)
    cost = models.IntegerField(blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_post_r8qmha', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
