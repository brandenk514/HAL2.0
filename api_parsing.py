class ApiParsing:
    def __init__(self):
        self.client = "me"

    def parse_for_lat_lng(self, location_request):
        """
        :param location_request: A list from a JSON request for a location
        :return: a tuple (Latitude, Longitude)
        """
        try:
            coordinates = []
            for location in location_request:
                coordinates.append(location['geometry']['location']['lat'])  # Latitude
                coordinates.append(location['geometry']['location']['lng'])  # Longitude
            tuple_coordinates = tuple(float(c) for c in coordinates)
            return tuple_coordinates
        except Exception:
            return "Coordinate parsing failed"

    def parse_location_for_address(self, location_request):
        """
        :param location_request: A list from a JSON request for a location
        :return: the address as a string
        """
        try:
            return location_request[1]['formatted_address']
        except Exception:
            return "Address parsing failed"

    def parse_timezone(self, timezone_request):
        """
        :parameter timezone_request: A list from a JSON request for a timezone
        :return timeZoneID as a String
        """
        try:
            return timezone_request['timeZoneId']
        except Exception:
            return "Timezone parsing failed"

    def parse_location_for_zip(self, location_request):
        """
        :parameter location_request: A list from a JSON request for a Zip code
        :return the zipcode as a String
        """
        zip_code = ""
        try:
            for l in location_request:
                zip_code = l['address_components'][7]
            code = zip_code['long_name']
            return code
        except Exception:
            return "Timezone parsing failed"

    def parse_elevation(self, elevation_request):
        """
        :param elevation_request: an elevation JSON request
        :return: elevation as a float
        """
        elevation = 0.0
        try:
            for e in elevation_request:
                elevation = e['elevation']
            return elevation
        except Exception:
            return "I could not find the elevation for the location you requested"
