from rest_framework import serializers
from .models import Notification, ActiveUnit

class NotificationSerializer(serializers.ModelSerializer):
    audio = serializers.FileField(
		max_length=None,
		use_url=True,
		required=False
	)
    class Meta:
        model = Notification
        fields = [
            'recipient_unit_id',
            'message_text',
            'license_plate',
            'audio'
        ]

class ActiveUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveUnit
        fields = [
            'unit_id',
            'latitude',
            'longitude',
            'last_seen'
        ]
