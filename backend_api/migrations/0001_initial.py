# Generated by Django 3.2.9 on 2022-01-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyWeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('temperature', models.CharField(blank=True, max_length=100, null=True)),
                ('max_temperature', models.CharField(blank=True, max_length=100, null=True)),
                ('min_temperature', models.CharField(blank=True, max_length=100, null=True)),
                ('humidity', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
