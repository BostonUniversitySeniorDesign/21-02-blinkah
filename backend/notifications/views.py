from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class NotificationList(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
