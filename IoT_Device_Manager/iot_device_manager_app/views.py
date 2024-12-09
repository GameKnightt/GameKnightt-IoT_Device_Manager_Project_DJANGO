from django.shortcuts import render
from .models import Sensor, Unit

# Create your views here.
def sensor_list(request):
    sensors = Sensor.objects.all()
    return render(request, 'sensor_list.html', {'sensors': sensors})

def unit_list(request):
    units = Unit.objects.all()
    return render(request, 'unit_list.html', {'units': units})

def sensor_detail(request, pk):
    sensor = Sensor.objects.get(pk=pk)
    return render(request, 'sensor_detail.html', {'sensor': sensor})

def unit_detail(request, pk):
    unit = Unit.objects.get(pk=pk)
    return render(request, 'unit_detail.html', {'unit': unit})