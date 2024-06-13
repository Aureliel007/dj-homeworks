from rest_framework import generics

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class SensorAPIListView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAPIView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer 
