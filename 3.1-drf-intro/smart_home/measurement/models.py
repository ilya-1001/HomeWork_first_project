from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.DecimalField(decimal_places=1, max_digits=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
