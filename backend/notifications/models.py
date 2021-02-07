from django.db import models

# Create your models here.

class Notification(models.Model):
    message_text = models.CharField(max_length=255)
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    license_plate = models.CharField(max_length=16)