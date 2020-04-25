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


def get_weather_states_icons(name):
    response = requests.get(f'https://www.metaweather.com/static/img/weather/png/64/{name}.png')
    if response.status_code == 200:
        with open(f"{name}.jpg", 'wb') as f:
            f.write(response.content)


def outline_forecast_main_data(raw_data):
    date = raw_data["time"][:10]
    lt_time = raw_data["time"][11:19]
    zone = raw_data["time"][-6:]
    utc_time = str(int(raw_data["time"][11:13]) - int(zone[:3])) + raw_data["time"][13:19]
    city = raw_data["title"].upper()

    report = f'''
Chosen city: {city} 
Current date: {date}
Current time: {lt_time}LT, {utc_time}UTC
Time zone: UTC {zone}

'''
    return report
