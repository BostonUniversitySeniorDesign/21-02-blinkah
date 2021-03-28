from django.shortcuts import render
from .models import Notification, ActiveUnit
from .serializers import NotificationSerializer, ActiveUnitSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class NotificationList(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationFilterUnitID(ListCreateAPIView):
    serializer_class = NotificationSerializer
    def get_queryset(self):
        return Notification.objects.filter(recipient_unit_id=self.kwargs['unit_id'])

class ActiveUnitList(ListCreateAPIView):
    queryset = ActiveUnit.objects.all()
    serializer_class = ActiveUnitSerializer

class ActiveUnitSerializer(RetrieveUpdateDestroyAPIView):
    queryset = ActiveUnit.objects.all()
    serializer_class = ActiveUnitSerializer

class ActiveUnitFilterUnitID(ListCreateAPIView):
    serializer_class = ActiveUnitSerializer
    def get_queryset(self):
        return ActiveUnit.objects.filter(unit_id=self.kwargs['unit_id'])

# TODO: Add filter class for latitude/longitude radius/bounding box
