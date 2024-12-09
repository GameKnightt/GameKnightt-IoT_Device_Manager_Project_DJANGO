from django.shortcuts import render, get_object_or_404, redirect
from .models import Sensor, Unit
from .forms import SensorForm, UnitForm

def sensor_list(request):
    sensors = Sensor.objects.all()
    return render(request, 'sensor_list.html', {'sensors': sensors})

def unit_list(request):
    units = Unit.objects.all()
    return render(request, 'unit_list.html', {'units': units})

def sensor_detail(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    return render(request, 'sensor_detail.html', {'sensor': sensor})

def unit_detail(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    return render(request, 'unit_detail.html', {'unit': unit})

def sensor_create(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sensor_list')
    else:
        form = SensorForm()
    return render(request, 'sensor_form.html', {'form': form})

def unit_create(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    else:
        form = UnitForm()
    return render(request, 'unit_form.html', {'form': form})

def sensor_update(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == 'POST':
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect('sensor_detail', pk=sensor.pk)
    else:
        form = SensorForm(instance=sensor)
    return render(request, 'sensor_form.html', {'form': form})

def unit_update(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_detail', pk=unit.pk)
    else:
        form = UnitForm(instance=unit)
    return render(request, 'unit_form.html', {'form': form})

def sensor_delete(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == 'POST':
        sensor.delete()
        return redirect('sensor_list')
    return render(request, 'sensor_confirm_delete.html', {'sensor': sensor})

def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        unit.delete()
        return redirect('unit_list')
    return render(request, 'unit_confirm_delete.html', {'unit': unit})