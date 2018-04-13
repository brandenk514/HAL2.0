from forecastiopy import *
import os
import api_parsing


class Weather:
    def __init__(self):
        self.disclaimer = "Powered by Dark Sky - https://darksky.net/poweredby/"
        self.parser = api_parsing.ApiParsing()
        self.api_key = os.environ.get('dark_sky_key')
        self.weather_obj = None

    def get_current_weather(self, location_requested):
        forecast_io = ForecastIO.ForecastIO(self.api_key, units=ForecastIO.ForecastIO.UNITS_US,
                                            lang=ForecastIO.ForecastIO.LANG_ENGLISH, latitude=location_requested[0],
                                            longitude=location_requested[1])
        if forecast_io.has_currently() is True:
            currently = FIOCurrently.FIOCurrently(forecast_io)
            self.weather_obj = currently
        else:
            print("No current forecast available")

    def get_current_summary(self):
        return self.weather_obj.summary

    def get_current_icon(self):
        return self.weather_obj.icon

    def get_current_temperature(self):
        return self.weather_obj.temperature

    def get_current_feels_like(self):
        return self.weather_obj.apparentTemperature

    def get_current_precipIntensity(self):
        return self.weather_obj.precipIntensity

    def get_current_precipProbability(self):
        return self.weather_obj.precipProbability


