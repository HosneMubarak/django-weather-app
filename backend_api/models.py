from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.utils import timezone


class DailyWeatherData(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100, null=True, blank=True)
    max_temperature = models.CharField(max_length=100, null=True, blank=True)
    min_temperature = models.CharField(max_length=100, null=True, blank=True)
    humidity = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name


class CityList(models.Model):
    city_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name


# Signal
def create_weather_data(sender, instance, created, **kwargs):
    """ when we will save data than city name will be saved in CityList Modal"""
    if created:
        CityList.objects.create(city_name=instance.city_name)


post_save.connect(create_weather_data, sender=DailyWeatherData)
