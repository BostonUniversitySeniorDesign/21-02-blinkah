# models.py
from django.db import models

class Incidents(models.Model):
    Plate = models.CharField(max_length=60)
    Latitude = models.CharField(max_length=60)
    Longitude = models.CharField(max_length=60)
    def __str__(self):
        return self.name
