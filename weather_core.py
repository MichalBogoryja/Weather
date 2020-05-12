import json
import requests
import os
from dataclasses import dataclass


@dataclass()
class OutlineWeather:
    city: str
    date: str
    time: str
    time_utc: str
    time_zone: str


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
    state_abbr: str


def get_location_id(city):
    response = requests.get(f'https://www.metaweather.com/api/location'
                            f'/search/?query={city}')
    city_id = json.loads(response.text)
    return city_id[0]['woeid']


def get_weather(city_id):
    response = requests.get(f'https://www.metaweather.com/api/location/'
                            f'{city_id}/')
    weather_data = json.loads(response.text)
    return weather_data


def get_weather_states_icons(name):
    response = requests.get(f'https://www.metaweather.com/static/img/weather/'
                            f'png/64/{name}.png')
    if response.status_code == 200:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dest_dir = os.path.join(script_dir, 'icons')
        try:
            os.makedirs(dest_dir)
        except OSError:
            pass  # already exists
        with open(os.path.join(dest_dir, f"{name}.jpg"), 'wb') as f:
            f.write(response.content)
    return dest_dir


def outline_forecast_main_data(raw_data):
    zone = raw_data["time"][-6:]
    utc_time = str(int(raw_data["time"][11:13]) - int(zone[:3])) \
        + raw_data["time"][13:19]
    forecast_outline = OutlineWeather(raw_data["title"].upper(),
                                      raw_data["time"][:10],
                                      raw_data["time"][11:19],
                                      utc_time,
                                      zone)

    return forecast_outline


def present_outline_weather(raw_data):
    forecast_outline = outline_forecast_main_data(raw_data)
    report = f'''
{'Chosen city:':>13} {forecast_outline.city}
{'Current date:':>13} {forecast_outline.date}
{'Current time:':>13} {forecast_outline.time}LT, {forecast_outline.time_utc}UTC
{'Time zone:':>13} UTC {forecast_outline.time_zone}'''

    return report


def analyse_weather(raw_data, day):
    raw_data = raw_data["consolidated_weather"][day]
    forecast = DailyWeather(raw_data["applicable_date"],
                            raw_data["weather_state_name"],
                            raw_data["the_temp"],
                            raw_data["wind_speed"],
                            raw_data["wind_direction_compass"],
                            raw_data["air_pressure"],
                            raw_data["humidity"],
                            raw_data["visibility"],
                            raw_data["predictability"],
                            raw_data["weather_state_abbr"])
    return forecast


def present_weather_daily(data, day, detail, metric):
    forecast_daily = analyse_weather(data, day)
    length_description = ['mi', 'km']
    speed_description = ['mph', 'km/h']
    change = [1, 1.609344]
    i = 1
    if not metric:
        i = 0

    report = f'''
{'Forecast for:':>15} {forecast_daily.date}
{'Weather state:':>15} {forecast_daily.state}
{'Temperature:':>15} {forecast_daily.temp:.1f}°C
{'Wind:':>15} {forecast_daily.wind_speed * change[i]:.2f} \
{forecast_daily.wind_dir} {speed_description[i]}'''

    if detail:
        report += f'''
{'Air pressure:':>15} {forecast_daily.pressure}mbar
{'Humidity:':>15} {forecast_daily.humidity}%
{'Visibility:':>15} {forecast_daily.visibility * change[i]:.1f}\
{length_description[i]}
{'Predictability:':>15} {forecast_daily.predictability}%'''

    return report
