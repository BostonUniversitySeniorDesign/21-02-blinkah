from django.db import models

def audioUploads(instance, filename):
	return '/'.join( ['audio', str(instance.id), filename])
    #return filename

class Notification(models.Model):
    recipient_unit_id = models.IntegerField()
    message_text = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=16)
    audio = models.FileField(upload_to=audioUploads, max_length=255, blank=True, null=True)

class ActiveUnit(models.Model):
    unit_id = models.IntegerField()
    latitude = models.DecimalField(decimal_places=4, max_digits=10)
    longitude = models.DecimalField(decimal_places=4,max_digits=10)
    last_seen = models.DateTimeField(auto_now=True)