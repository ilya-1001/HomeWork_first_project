from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import CreateSensorSerializer, UpdateSensorSerializer, \
                         AddMeasurementSerializer, MeasurementSerializer, \
                         SensorsSerializer, SensorDetailSerializer


class CreateSensorsView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = CreateSensorSerializer


class UpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = UpdateSensorSerializer


class AddMeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = AddMeasurementSerializer


class ListSensorsSerializerView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class ListSensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
