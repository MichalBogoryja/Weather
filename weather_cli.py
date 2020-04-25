import argparse
from weather_core import get_location_id, get_weather, outline_forecast_main_data, analyse_weather


def forecast_range_check(days, max_days):
    if days > max_days:
        days = max_days
        print(f'The maximum forecast range is {max_days}')
    return days


my_parser = argparse.ArgumentParser(prog='weather_cli',
                                    usage='%(prog)s [city name]',
                                    description='Shows the weather forecast in the desired city',
                                    epilog='Enjoy!')

my_parser.version = '1.0'

my_parser.add_argument('-City',
                       metavar='Name of the city',
                       type=str,
                       default='warsaw',
                       help='Name of the city for the weather forecast')

my_parser.add_argument('-Range',
                       metavar='The range of the forecast',
                       type=int,
                       default=3,
                       help='The range of the requested forecast')

my_parser.add_argument('-ver',
                       action='version')

args = my_parser.parse_args()

city = args.City
forecast_range = args.Range

city_id = get_location_id(city)

weather_data = get_weather(city_id)

forecast_range = forecast_range_check(forecast_range, len(weather_data["consolidated_weather"]))

forecast_data = outline_forecast_main_data(weather_data)

print(forecast_data)

