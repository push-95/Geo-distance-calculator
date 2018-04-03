import unittest
import sys
from dist_calc import Geocode

class TestDistCalcOutput(unittest.TestCase):

	addr1 = '1600 Amphitheatre Parkway, Mountain View, CA'
	addr2 = '1550 Carnavon Way, San Jose, CA'
	key = ''

	if key is '':
		print "Please enter the API key in the code"
		exit()

	lat = 40.714224
	lng = -73.961452

	def test_wrong_api_key(self):
		# print 'Invalid API key'
		addr1 = self.addr1
		addr2 = self.addr2
		key = '1234'
		g1 = Geocode(addr1, key)
		g2 = Geocode(addr2, key)
		self.assertEqual(g1.calc_dist(g2)[0], 'REQUEST_DENIED')

	def test_same_address(self):
		# print 'Distance to same address'
		addr1 = self.addr1
		key = self.key
		g1 = Geocode(addr1, key)
		g2 = Geocode(addr1, key)
		self.assertEqual(g1.calc_dist(g2)[2], 0.0)

	def test_known_dist(self):
		# print 'Distance between known addresses'
		addr1 = self.addr1
		addr2 = self.addr2
		key = self.key
		g1 = Geocode(addr1, key)
		g2 = Geocode(addr2, key)
		self.assertEqual(g1.calc_dist(g2)[2], 18.013572318312274)

	def test_latlng_known_addr(self):
		# print 'latlng of known address'
		addr = self.addr1
		key = self.key
		g1 = Geocode(addr, key)
		self.assertEqual(g1.geocode(addr)['lat'], 37.4224082)
		self.assertEqual(g1.geocode(addr)['lng'], -122.0856086)

	def test_addr_known_latlng(self):
		# print 'address of known latlng'
		# initialized address does not matter
		addr = self.addr1
		key = self.key
		g1 = Geocode(addr, key)
		lat = self.lat
		lng = self.lng
		latlng = '{},{}'.format(lat, lng)
		address = g1.reverse_geocode(latlng)['address']
		self.assertEqual(address, '277 Bedford Ave, Brooklyn, NY 11211, USA')

if __name__ == '__main__':
	unittest.main()