import requests
from django.db import models
from django.db.models.signals import post_save

# weather api key
from requests import Response
from rest_framework import status

from weather_api_project import settings

API_KEY = settings.API_KEY

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
    city = models.ForeignKey(DailyWeatherData, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    city_lat = models.CharField(max_length=100, null=True, blank=True)
    city_lon = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city.city_name


# Signal
def create_weather_data(sender, instance, created, **kwargs):
    """ when we will save data than city name will be saved in CityList Modal"""
    if created:
        lat = ''
        lon = ''
        try:
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + instance.city_name + "&appid=e8bff08e3d5cea9e0b750a3bfe62f05e"
            response = requests.post(url)
            # extracting data from api
            lon = response.json()['coord']['lon']
            lat = response.json()['coord']['lat']
        except:
            print('nno data found')
        CityList.objects.create(city=instance, name=instance.city_name, city_lat=lat, city_lon=lon)


post_save.connect(create_weather_data, sender=DailyWeatherData)
