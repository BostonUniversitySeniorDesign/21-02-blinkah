from django.shortcuts import render
# views.py
from rest_framework import viewsets
from rest_framework import serializers

from .serializers import IncidentSerializer
from .models import Incidents


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incidents.objects.all().order_by('Plate')
    serializer_class = IncidentSerializer
# Create your views here.
