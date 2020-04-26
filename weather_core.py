import json
import requests

from dataclasses import dataclass


@dataclass()
class Weather:
    description: str
    value: str


@dataclass()
class DailyWeather:
    date: str
    state: str
    temp: float
    wind_speed: float
    wind_dir: str
    pressure: str
    humidity: str
    visibility: float
    predictability: float

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
    city = Weather('Chosen city: ', raw_data["title"].upper())

    report = f'''
{city.description}{city.value} 
Current date: {date}
Current time: {lt_time}LT, {utc_time}UTC
Time zone: UTC {zone}
'''
    return report


def analyse_weather(raw_data, day, details):
    raw_data = raw_data["consolidated_weather"][day]
    forecast = DailyWeather(raw_data["applicable_date"], raw_data["weather_state_name"], raw_data["the_temp"],
                            raw_data["wind_speed"] * 1.609344, raw_data["wind_direction_compass"],
                            raw_data["air_pressure"], raw_data["humidity"], raw_data["visibility"] * 1.609344,
                            raw_data["predictability"])
    report = f'''
Forecast for: {forecast.date}
Weather state: {forecast.state}
Temperature: {forecast.temp:.1f}°C
Wind: {forecast.wind_speed:.2f} {forecast.wind_dir} [km/h]'''

    if details:
        report += f'''
Air pressure: {forecast.pressure}mbar
Humidity: {forecast.humidity}%
Visibility: {forecast.visibility:.1f}km
Predictability: {forecast.predictability}%
'''
    return report
