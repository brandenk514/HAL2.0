import motion_sensor
import weather
import location


class Hal:
    def __init__(self):
        # self.motion_sensor = motion_sensor.MotionSensor()
        self.location_request = location.Location()
        self.weather_request = weather.Weather()


if __name__ == '__main__':
    hal = Hal()
    locale = hal.location_request.create_location_request("1021 Dulaney Valley Road, Towson, MD, 21204")
    print(locale)
    coordinates = hal.location_request.parsing.parse_for_lat_lng(locale)
    print(coordinates)
    weather = hal.weather_request.get_current_weather(coordinates)
    print(weather.temperature)
