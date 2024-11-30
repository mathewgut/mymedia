from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class SpotifyProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='spotify_profile'
    )
    auth_token = models.CharField(max_length=900)
    refresh_token = models.CharField(max_length=900, blank=True, null=True)
    token_expires_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"SpotifyProfile for {self.user.username}"