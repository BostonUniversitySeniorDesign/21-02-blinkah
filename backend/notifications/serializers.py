from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'message_text',
            'latitude',
            'longitude',
            'license_plate'
        ]