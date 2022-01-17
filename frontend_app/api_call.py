import requests
from django.shortcuts import render
from requests.exceptions import HTTPError

from django.conf import settings

# base url for the api url from setting file
BASE_URL = settings.API_BASE_URL


# Get weather info by city name
def get_weather_api(**args):
    """
    get weather data by city name
    """
    try:
        get_weather_api_url = BASE_URL + "/api/current_weather_by_city_name/"

        response = requests.post(
            get_weather_api_url,
            headers={
                "Content-Type": "application/json",
            },
            json={
                "city_name": args['city_name'],
            },
            verify=False
        )

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'get_weather_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'get_weather_api(): Other error occurred: {err}')
    else:
        print('get_weather_api(): Success!')

    return response


def save_daily_weather_data(**args):
    try:
        url = BASE_URL + "/api/daily_weather_data/"
        response = requests.post(url,
                                 json={
                                     "city_name": args['city_name'],
                                     "temperature": args['temperature'],
                                     "max_temperature": args['max_temperature'],
                                     "min_temperature": args['min_temperature'],
                                     "humidity": args['humidity']
                                 },
                                 )

        response.raise_for_status()

    except HTTPError as http_error:
        print(f"save_daily_weather_data():{http_error}")
    except Exception as err:
        print(f"save_daily_weather_data():{err}")
    else:
        print("save_daily_weather_data() success")
    return response


def get_daily_weather_data(**args):
    try:
        url = BASE_URL + "/api/daily_weather_data/"
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError as http_error:
        print(f"get_daily_weather_data():{http_error}")
    except Exception as err:
        print(f"get_daily_weather_data():{err}")
    else:
        print("get_daily_weather_data() success")
    return response


def get_city_list(**args):
    try:
        url = BASE_URL + "/api/city_list/"
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError as http_error:
        print(f"get_city_list():{http_error}")
    except Exception as err:
        print(f"get_city_list():{err}")
    else:
        print("get_city_list() success")
    return response


def get_single_daily_weather_data(**args):
    try:
        url = BASE_URL + "/api/daily_weather_data/" + args['id']
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError as http_error:
        print(f"get_single_daily_weather_data():{http_error}")
    except Exception as err:
        print(f"get_single_daily_weather_data():{err}")
    else:
        print("get_single_daily_weather_data() success")
    return response


def update_save_daily_weather_data(**args):
    try:
        url = BASE_URL + "/api/daily_weather_data/" + args['id'] + '/'
        response = requests.put(url,
                                json={
                                    "city_name": args['city_name'],
                                    "temperature": args['temperature'],
                                    "max_temperature": args['max_temperature'],
                                    "min_temperature": args['min_temperature'],
                                    "humidity": args['humidity']
                                },
                                )

        response.raise_for_status()

    except HTTPError as http_error:
        print(f"update_save_daily_weather_data():{http_error}")
    except Exception as err:
        print(f"update_save_daily_weather_data():{err}")
    else:
        print("update_save_daily_weather_data() success")
    return response


def delete_save_daily_weather_data(**args):
    try:
        url = BASE_URL + "/api/daily_weather_data/" + args['id']
        response = requests.delete(url)

        response.raise_for_status()

    except HTTPError as http_error:
        print(f"delete_save_daily_weather_data():{http_error}")
    except Exception as err:
        print(f"delete_save_daily_weather_data():{err}")
    else:
        print("delete_save_daily_weather_data() success")
    return response
