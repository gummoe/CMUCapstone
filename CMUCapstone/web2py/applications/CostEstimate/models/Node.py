import urllib2
import json


class Node(object):

    def __init__(self, address):
        self.address = address
        self.latitude = 0
        self.longitude = 0

    def get_lat(self):
        return self.latitude

    def get_long(self):
        return self.longitude

    def geocode(self):
        formatted_address = self.address.replace(' ', '+')
        url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=" + formatted_address
        content = urllib2.urlopen(url).read()
        json_doc = json.loads(content)
        self.latitude = json_doc["results"][0]["geometry"]['location']['lat']
        self.longitude = json_doc["results"][0]["geometry"]['location']['lng']

    def __str__(self):
        return self.address
