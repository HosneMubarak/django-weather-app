from django.shortcuts import render, redirect
from .api_call import get_weather_api, save_daily_weather_data, get_daily_weather_data, get_single_daily_weather_data, \
    update_save_daily_weather_data, delete_save_daily_weather_data, get_city_list


# This is home function for selecting city name and show the daily results
def home(request):
    # Initialize the variable as empty
    context = {
        'weather_data': '',
        'msg': ''
    }
    if 'search' in request.POST:
        # Getting city name from the search form....
        api_data = get_weather_api(city_name=request.POST.get('city_name'))
        # If response is success then data pass to the html page
        if api_data.status_code == 200:
            context = {
                'weather_data': api_data.json(),
            }
            return render(request, 'index.html', context)
        # If response is not success then pass the empty dict and message
        else:
            context = {
                'weather_data': '',
                'msg': 'Please enter a valid city !'
            }
            return render(request, 'index.html', context)
    elif 'save' in request.POST:
        if request.POST:
            # getting data from html form
            city_name = request.POST.get('city_name')
            temperature = request.POST.get('temperature')
            max_temperature = request.POST.get('max_temperature')
            min_temperature = request.POST.get('min_temperature')
            humidity = request.POST.get('humidity')
            # saving data calling api
            save_data_response = save_daily_weather_data(city_name=city_name, temperature=temperature,
                                                         max_temperature=max_temperature,
                                                         min_temperature=min_temperature,
                                                         humidity=humidity)
            print(city_name, save_data_response.json())
            if save_data_response.status_code == 201:
                return redirect('frontend_app:weather-data-list')
            else:
                return redirect(request.get_full_path())
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)


def weather_data_list(request):
    # getting data from calling api
    all_save_weather_data = get_daily_weather_data()
    city_list = get_city_list()
    context = {
        'all_save_weather_data': all_save_weather_data.json(),
        'city_list': city_list.json()
    }
    return render(request, 'weather_data_list.html', context)


def weather_details(request, id):
    # getting data from calling api
    single_save_weather_data = get_single_daily_weather_data(id=str(id))
    if request.POST:
        city_name = request.POST.get('city_name')
        temperature = request.POST.get('temperature')
        max_temperature = request.POST.get('max_temperature')
        min_temperature = request.POST.get('min_temperature')
        humidity = request.POST.get('humidity')
        update_save_data_response = update_save_daily_weather_data(id=id, city_name=city_name, temperature=temperature,
                                                                   max_temperature=max_temperature,
                                                                   min_temperature=min_temperature,
                                                                   humidity=humidity)
        print(city_name, update_save_data_response.json())
        if update_save_data_response.status_code == 200:
            return redirect('frontend_app:weather-data-list')
        else:
            return redirect(request.get_full_path())
    context = {
        'single_save_weather_data': single_save_weather_data.json()
    }
    return render(request, 'weather_data_details.html', context)


def delete(request, id):
    # deleteing data using delete api
    delete_response = delete_save_daily_weather_data(id=id)
    if delete_response.status_code == 204:
        return redirect('frontend_app:weather-data-list')
    else:
        return redirect(request.get_full_path())
