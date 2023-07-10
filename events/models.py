from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Event model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    category = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255, blank=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(
        upload_to='images/', default='../default_post_r8qmha', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
