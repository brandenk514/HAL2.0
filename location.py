import googlemaps
import os
import requests
import json
import api_parsing


class Location:
    def __init__(self):
        self.client = googlemaps.Client(key=os.environ.get('google_api_key'))
        self.parsing = api_parsing.ApiParsing()

    def create_location_request(self, location):
        """
        :param location: a string of an address
        :return: a location JSON request as a list
        """
        try:
            return self.client.geocode(location)
        except googlemaps.exceptions.ApiError:
            return "geocode API Error"
        except googlemaps.exceptions.HTTPError:
            return "geocode HTTP Error"
        except googlemaps.exceptions.Timeout:
            return "geocode Timeout Error"
        except googlemaps.exceptions.TransportError:
            return "geocode Transport Error"

    def create_ip_location_request(self):
        """
        Gets the lat, lng for a give IP
        :return:
        """
        try:
            r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=" +
                              os.environ.get('google_api_key')).text
            return json.loads(r)
        except googlemaps.exceptions.ApiError:
            return "geocode API Error"
        except googlemaps.exceptions.HTTPError:
            return "geocode HTTP Error"
        except googlemaps.exceptions.Timeout:
            return "geocode Timeout Error"
        except googlemaps.exceptions.TransportError:
            return "geocode Transport Error"

    def create_timezone_request(self, location):
        """
        :param location As a list
        :return: a timezone JSON request
        """
        coordinates = self.parsing.parse_for_lat_lng(location)
        try:
            return self.client.timezone(coordinates)
        except googlemaps.exceptions.ApiError:
            return "timezone API Error"
        except googlemaps.exceptions.HTTPError:
            return "timezone HTTP Error"
        except googlemaps.exceptions.Timeout:
            return "timezone Timeout Error"
        except googlemaps.exceptions.TransportError:
            return "timezone Transport Error"

    def create_elevation_request(self, location):
        """
        :param location as a list
        :return: a elevation JSON request
        """
        coordinates = self.parsing.parse_for_lat_lng(location)
        try:
            return self.client.elevation(coordinates)
        except googlemaps.exceptions.ApiError:
            return "elevation API Error"
        except googlemaps.exceptions.HTTPError:
            return "elevation HTTP Error"
        except googlemaps.exceptions.Timeout:
            return "elevation Timeout Error"
        except googlemaps.exceptions.TransportError:
            return "elevation Transport Error"

    def create_distance_matrix_request(self, origin, destination):
        """
        :param origin: A location String
        :param destination: A location String
        :return: A directions
        """
        try:
            return self.client.distance_matrix(origin, destination)
        except googlemaps.exceptions.ApiError:
            return "distance_matrix API Error"
        except googlemaps.exceptions.HTTPError:
            return "distance_matrix HTTP Error"
        except googlemaps.exceptions.Timeout:
            return "distance_matrix Timeout Error"
        except googlemaps.exceptions.TransportError:
            return "distance_matrix Transport Error"

    def get_distance_between_to_locations(self, distance_request):
        """
        :param distance_request: A string
        :return:  A string consisting of distance and travel time between two locations in a given radius
        """
        locations = self.f.split_locations(self.f.split_sentence(distance_request))
        distance_matrix = self.create_distance_matrix_request(locations[0], locations[1])
        destination = distance_matrix['destination_addresses'][0]
        ori = distance_matrix['origin_addresses'][0]
        rows = distance_matrix['rows'][0]
        distance = ""
        time = ""
        for e in rows['elements']:
            if e['status'] == "ZERO_RESULTS":
                return "The distance between {0} and {1} is too far to calculate".format(ori, destination)
            distance = e['distance']['text']
            time = e['duration']['text']
        return "The distance between {0} and {1} is approximately {2} and it will take about {3} in travel time by car"\
            .format(ori, destination, distance, time)


if __name__ == '__main__':
    loc = Location()
    locale = loc.create_location_request("London, England")
    print(locale)
    req = loc.create_elevation_request(locale)
    response = loc.parsing.parse_elevation(req)
    print(response)
