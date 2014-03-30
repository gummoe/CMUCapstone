import urllib2
import json
from numpy import matrix


class NodeMatrix(object):

    def __init__(self, node_list):
        self.node_list = node_list
        self.duration_matrix = None
        self.distance_matrix = None
        self.duration_array = None
        self.distance_array = None

    def get_matrix(self):
        addresses = ""
        for node in self.node_list:
            formatted_address = node.address.replace(' ', '+')
            addresses += formatted_address + "|"
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?key=AIzaSyArKgjL2En05_5xsxgA4XoCKNfXd50fL-8&sensor=false&origins=" + addresses + "&destinations=" + addresses

        content = urllib2.urlopen(url).read()
        json_doc = json.loads(content)
        #print json_doc
        address_rows = json_doc["rows"]

        duration_rows = []
        distance_rows = []
        for row in address_rows:
            elements = row['elements']
            duration_list = []
            distance_list = []
            for item in elements:
                duration_list.append(item['duration']['value'])
                distance_list.append(item['distance']['value'])
            duration_rows.append(duration_list)
            distance_rows.append(distance_list)
        self.duration_matrix = matrix(duration_rows)
        self.distance_matrix = matrix(distance_rows)
        self.duration_array = duration_rows
        self.distance_array = distance_rows
        print "This is the duration array:"
        print duration_rows

