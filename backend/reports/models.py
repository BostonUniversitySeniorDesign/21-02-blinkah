from django.db import models

# Create your models here.

class Report(models.Model):
    license_plate = models.CharField(max_length=16)
    speed = models.IntegerField()
    infraction = models.CharField() # TO BE CHANGED ?
    confidence = models.DecimalField()
    timestamp = models.CharField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    #photograph = models.ImageField(upload_to="report_captures")
    unit_id = models.IntegerField()

class Statistics(models.Model):
    total_reports = models.IntegerField()
    avg_confidence = models.DecimalField()
    last_updated = models.DateTimeField(auto_now=True)

