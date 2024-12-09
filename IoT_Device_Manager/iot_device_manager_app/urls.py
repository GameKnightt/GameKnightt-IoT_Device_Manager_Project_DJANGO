from django.urls import path
from .views import sensor_list, unit_list, sensor_detail, unit_detail

urlpatterns = [
    path('sensors/', sensor_list, name='sensor_list'),
    path('units/', unit_list, name='unit_list'),
    path('sensors/<int:pk>/', sensor_detail, name='sensor_detail'),
    path('units/<int:pk>/', unit_detail, name='unit_detail'),
]