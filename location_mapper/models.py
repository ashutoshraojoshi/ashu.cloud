# location_mapper/models.py

from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    custom_name = models.CharField(max_length=255, unique=True)
    google_maps_url = models.URLField()  # Field for Google Maps URL
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.custom_name
