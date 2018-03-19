from forecastiopy import *
import os
import location
import api_parsing


class Weather:
    def __init__(self):
        self.disclaimer = "Powered by Dark Sky - https://darksky.net/poweredby/"
        self.location = location.Location()
        self.parser = api_parsing.ApiParsing()
        self.api_key = os.environ.get('dark_sky_key')

    def get_current_weather(self, location_requested):
        forecast_io = ForecastIO.ForecastIO(self.api_key, units=ForecastIO.ForecastIO.UNITS_US,
                                            lang=ForecastIO.ForecastIO.LANG_ENGLISH, latitude=location_requested[0],
                                            longitude=location_requested[1])
        if forecast_io.has_currently() is True:
            currently = FIOCurrently.FIOCurrently(forecast_io)
            return currently
        else:
            print("No current forecast available")
