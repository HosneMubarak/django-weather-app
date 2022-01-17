from django.contrib import admin
from .models import DailyWeatherData, CityList


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'date')
    list_filter = ('id', 'city_name',)
    date_hierarchy = 'date'
    list_per_page = 10


admin.site.register(DailyWeatherData, ImageAdmin)
admin.site.register(CityList)
