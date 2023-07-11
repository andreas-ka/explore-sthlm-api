from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Attend(models.Model):
    """
    Attend model, related to User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='attend', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.owner} {self.event}'