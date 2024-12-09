from django.db import models

# Create your models here.

class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    longi = models.FloatField()  # Longitude
    lati = models.FloatField()  # Latitude
    period = models.IntegerField()

class Measure(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    timestamp = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measures')

class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Metric(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
