from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import DailyWeatherData, CityList


class DailyWeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWeatherData
        fields = "__all__"


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityList
        fields = "__all__"
