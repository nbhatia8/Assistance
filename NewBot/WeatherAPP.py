import pyowm
from config_reader import ConfigReader


class WeatherInformation:
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        self.owmapikey = self.configuration['119242c426975bc98ee4f259b9551823']
        self.owm = pyowm.OWM(self.owmapikey)

    def get_weather_info(city):
        # config_reader = ConfigReader()
        # configuration = config_reader.read_config()
        owmapikey = '119242c426975bc98ee4f259b9551823'
        owm = pyowm.OWM(owmapikey)
        # city = city

        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        latlon_res = observation.get_location()
        lat = str(latlon_res.get_lat())
        lon = str(latlon_res.get_lon())

        wind_res = w.get_wind()
        wind_speed = str(wind_res.get('speed'))

        humidity = str(w.get_humidity())

        celsius_result = w.get_temperature('celsius')
        temp_min_celsius = str(celsius_result.get('temp_min'))
        temp_max_celsius = str(celsius_result.get('temp_max'))

        fahrenheit_result = w.get_temperature('fahrenheit')
        temp_min_fahrenheit = str(fahrenheit_result.get('temp_min'))
        temp_max_fahrenheit = str(fahrenheit_result.get('temp_max'))
        bot_says = "Today the weather in " + city + " is :\n Maximum Temperature :" + temp_max_celsius + " Degree Celsius" + ".\n Minimum Temperature :" + temp_min_celsius + " Degree Celsius" + ": \n" + "Humidity :" + humidity + "%"
        return bot_says
