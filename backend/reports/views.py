from django.shortcuts import render
from .models import Report, Statistics
from .serializers import ReportSerializer, StatisticsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

class ReportList(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetail(RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

# We only deal with one statistics object, so no need for list view
class StatisticsDetail(RetrieveUpdateAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
