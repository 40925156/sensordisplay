from django.shortcuts import render
from sensor.models import Temperature
from sensor.serializers import TempSerializer
from rest_framework import generics
# Create your views here.
class temperature_api(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TempSerializer