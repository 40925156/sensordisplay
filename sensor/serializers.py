from sensor.models import Temperature
from rest_framework import serializers
class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['captime', 'captemperature']

