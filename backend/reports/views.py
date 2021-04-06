import django_filters.rest_framework
from django.shortcuts import render
from .models import Report, Statistics
from .serializers import ReportSerializer, StatisticsSerializer
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

class ReportList(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    

class ReportDetail(RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

# The following two filters are the only ones needed currently, additional ones can be added by necessity

class ReportFilterUnitID(ListCreateAPIView):
    serializer_class = ReportSerializer
    def get_queryset(self):
        return Report.objects.filter(unit_id=self.kwargs['unit_id'])
    
class ReportFilterLicensePlate(ListCreateAPIView):
    serializer_class = ReportSerializer
    def get_queryset(self):
        return Report.objects.filter(license_plate=self.kwargs['license_plate'])
    
# We only deal with one statistics object, so no need for list view
class StatisticsDetail(RetrieveUpdateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
