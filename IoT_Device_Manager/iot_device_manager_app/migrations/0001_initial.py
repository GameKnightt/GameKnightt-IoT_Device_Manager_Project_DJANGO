# Generated by Django 5.1.4 on 2024-12-09 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('longi', models.IntegerField()),
                ('lati', models.IntegerField()),
                ('period', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measures', to='iot_device_manager_app.sensor')),
            ],
        ),
    ]