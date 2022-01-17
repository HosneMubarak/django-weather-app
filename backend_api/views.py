from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from requests.exceptions import HTTPError
from rest_framework import generics
from .models import DailyWeatherData, CityList
from .serializers import DailyWeatherDataSerializer, CityListSerializer

# weather api key
API_KEY = "e8bff08e3d5cea9e0b750a3bfe62f05e"


@api_view(['GET', 'POST'])
def get_current_weather_by_city_name(request):
    """

    Get current weather of given city

    """
    if request.data:
        city_name = request.data['city_name']
        try:
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=e8bff08e3d5cea9e0b750a3bfe62f05e"
            response = requests.post(url)
            response.raise_for_status()

        except HTTPError as http_error:
            print(f"get_current_weather_by_city_name():{http_error}")
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        except Exception as err:
            print(f"get_current_weather_by_city_name():{err}")
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        else:
            print("get_current_weather_by_city_name() success")
        return Response(status=status.HTTP_200_OK, data=response.json())
    else:
        return Response(status=status.HTTP_200_OK,
                        data='PLease pass the city name {city_name: your_city_name}')


class DailyWeatherDataList(generics.ListCreateAPIView):
    queryset = DailyWeatherData.objects.all()
    serializer_class = DailyWeatherDataSerializer


class DailyWeatherDataDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyWeatherData.objects.all()
    serializer_class = DailyWeatherDataSerializer


class CityListView(generics.ListAPIView):
    queryset = CityList.objects.all()
    serializer_class = CityListSerializer
