from django.db import models

class Notification(models.Model):
    message_text = models.CharField(max_length=255)
    latitude = models.DecimalField(decimal_places=4,max_digits=10)
    longitude = models.DecimalField(decimal_places=4,max_digits=10)
    license_plate = models.CharField(max_length=16)