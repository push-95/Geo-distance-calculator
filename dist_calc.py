import requests
import math

class Geocode(object):

    geodata = None
    key = None
    reverse = False
    url = None
    def __init__(self, addr, key, reverse=False):
    
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.reverse = reverse
        self.key = key
        if reverse:
            self.geodata = self.reverse_geocode(addr)
        else:
            self.geodata = self.geocode(addr)

    def set_key(self, key):
        self.key = key
        return 

    def geocode(self, address):    
        key = self.key
        params = {}
        params['address'] = address
        params['sensor'] = 'false'
        params['key'] = key
        req = requests.get(self.url, params=params)
        res = req.json()
        if (res['status'] == 'REQUEST_DENIED'):
            return 'REQUEST_DENIED'
        result = res['results'][0]
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        return geodata

    def reverse_geocode(self, latlng):
        url = self.url
        key = self.key
        params = {}
        params['latlng'] = latlng
        params['sensor'] = 'true'
        params['key'] = key
        req = requests.get(url, params=params)
        res = req.json()
        if (res['status'] == 'REQUEST_DENIED'):
            return 'REQUEST_DENIED'
        result = res['results'][0]
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        return geodata

    def distance(self, lat1, lng1, lat2, lng2):
        radius = 6371 # km
        dlat = math.radians(float(lat2) - float(lat1))
        dlng = math.radians(float(lng2) - float(lng1))
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng/2) * math.sin(dlng/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d

    def calc_dist(self, GCode):
        geodata1 = self.geodata
        geodata2 = GCode.geodata
        if geodata1 == 'REQUEST_DENIED' or geodata2 == 'REQUEST_DENIED':
            return 'REQUEST_DENIED', '0', '0'
        return (geodata1['address'], geodata2['address'], self.distance(geodata1['lat'], geodata1['lng'], geodata2['lat'], geodata2['lng']))

if __name__ == '__main__':
    key = ''

    if key is '':
        print "Please enter the API key in the code"
        exit()
    
    g1 = Geocode('455 14th Street NW, Atlanta, GA', key)
    g2 = Geocode('470 16th Street NW, Atlanta, GA', key)

    addr1, addr2, dist = g1.calc_dist(g2)

    print dist