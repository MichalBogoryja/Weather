import json
import requests


def get_location_id(city):
    response = requests.get(f'https://www.metaweather.com/api/location/search/?query={city}')
    city_id = json.loads(response.text)
    return city_id[0]['woeid']


def get_weather(city_id):
    response = requests.get(f'https://www.metaweather.com/api/location/{city_id}/')
    weather_data = json.loads(response.text)
    return weather_data



