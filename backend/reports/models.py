from django.db import models

# Create your models here.

def reportCaptures(instance, filename):
	return '/'.join( ['captures', str(instance.id), filename])
    #return filename

class Report(models.Model):
    license_plate = models.CharField(max_length=16)
    speed = models.IntegerField()
    infraction = models.CharField(max_length=255) # TO BE CHANGED ?
    confidence = models.DecimalField(decimal_places=4,max_digits=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(decimal_places=4,max_digits=10)
    longitude = models.DecimalField(decimal_places=4,max_digits=10)
    photograph = models.ImageField(upload_to=reportCaptures, max_length=255, blank=True, null=True)
    unit_id = models.IntegerField()

class Statistics(models.Model):
    total_reports = models.IntegerField()
    avg_confidence = models.DecimalField(decimal_places=4,max_digits=10)
    last_updated = models.DateTimeField(auto_now=True)

