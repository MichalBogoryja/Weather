import argparse
from weather_core import get_location_id, get_weather, \
    present_weather_daily, present_outline_weather


def forecast_range_check(days, max_days):
    if days > max_days:
        days = max_days
        print(f'The maximum forecast range is {max_days}')
    return days


my_parser = argparse.ArgumentParser(prog='weather_cli',
                                    usage='%(prog)s [city name]',
                                    description='Shows the weather forecast '
                                                'in the desired city',
                                    epilog='Enjoy!')

my_parser.version = '1.0'

my_parser.add_argument('City',
                       metavar='Name of the city',
                       type=str,
                       help='Name of the city for the weather forecast')

my_parser.add_argument('-Range',
                       metavar='The range of the forecast',
                       type=int,
                       default=3,
                       help='The range of the requested forecast')

my_parser.add_argument('-Detailed',
                       action="store_false",
                       help='''The level of the forecast's details
                        can be adjusted. If this argument is not provided
                        than the level of details is high''')

my_parser.add_argument('-Imperial',
                       action="store_false",
                       help='''Units can be changed, metric or imperial.
                        If this argument is not provided than units are
                        metric''')

my_parser.add_argument('-ver',
                       action='version')

args = my_parser.parse_args()

city = args.City
forecast_range = args.Range
details = args.Detailed
metric = args.Imperial

city_id = get_location_id(city)

weather_data = get_weather(city_id)

forecast_range = forecast_range_check(forecast_range,
                                      len(weather_data["consolidated_weather"])
                                      )

forecast_data = present_outline_weather(weather_data)

print(forecast_data)

for i in range(forecast_range):
    print(present_weather_daily(weather_data, i, details, metric))
