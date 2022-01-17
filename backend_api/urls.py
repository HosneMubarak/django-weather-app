from django.urls import path
from .views import get_current_weather_by_city_name, DailyWeatherDataList, DailyWeatherDataDetails, CityListView

app_name = 'backend_api'

urlpatterns = [
    path('current_weather_by_city_name/', get_current_weather_by_city_name),
    path('daily_weather_data/', DailyWeatherDataList.as_view()),
    path('city_list/', CityListView.as_view()),
    path('daily_weather_data/<int:pk>/', DailyWeatherDataDetails.as_view()),
]
