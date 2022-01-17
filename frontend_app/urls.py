from django.urls import path
from .views import home, weather_data_list, weather_details, delete

app_name = 'frontend_app'

urlpatterns = [
    path('', home, name='home'),
    path('weather_data_list/', weather_data_list, name='weather-data-list'),
    path('weather_data_list/<id>/', weather_details, name='weather-data-list-details'),
    path('weather_data_delete/<id>/', delete, name='weather-data-list-delete'),
]
