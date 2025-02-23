from django.urls import path
from measurement.views import ListSensorsSerializerView, CreateSensorsView, \
    ListSensorDetailView, MeasurementView, UpdateSensorView

urlpatterns = [
    path('createsensors/', CreateSensorsView.as_view()),
    path('sensors/', ListSensorsSerializerView.as_view()),
    path('sensor/<pk>/', ListSensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
