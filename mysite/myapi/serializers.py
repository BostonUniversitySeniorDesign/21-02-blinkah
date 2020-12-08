# serializers.py
from rest_framework import serializers
from rest_framework.serializers import *

from .models import Incidents

class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incidents
        fields = ('Plate', 'Latitude', 'Longitude')

