from rest_framework import serializers
from .models import Report, Statistics

class ReportSerializer(serializers.ModelSerializer):
	photograph = serializers.ImageField(
		max_length=None,
		use_url=True
	)
	class Meta:
		model = Report
		fields = [
			'id',
			'license_plate',
			'speed',
			'infraction',
			'confidence',
			'latitude',
			'longitude',
			'unit_id',
			'photograph',
			'timestamp'
        ]

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = [
            'total_reports',
            'avg_confidence'
        ]
