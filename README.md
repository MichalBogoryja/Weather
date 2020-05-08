# Weather

Weather is a basic Python app for getting weather forecasts for the desired city. It has two versions: GUI and console. 



# Installation

- copy repository and unpack
- install all requirements (pip install ...)



# Usage

### Cli

```
weather_cli -h
usage: 
weather_cli [city name]  Shows the weather forecast in the desired city  

positional arguments:                                                    
Name of the city     Name of the city for the weather forecast         

optional arguments:                                                     
-h, --help           Show this help message and exit                   
-Range   			 The range of the requested forecast   
-Detailed            The level of the forecast's details can be adjusted. If this 							 argument is not provided than the level of details is high
-Imperial			 Units can be changed, metric or imperial. If this argument is not 						 provided than units are metric
-ver                 Show program's version number and exit                                                                                     Enjoy!  
```

### GUI

1. In adequate text box  provide:
   - Name of the city (default == 'Warsaw')
   - Length of the forecast (default == 3)
2. Check radio-button corresponding desired level detail (default == 'no details')
3. Check radio-button corresponding desired units (default == 'metric')
4. Press 'Show forecast' 

