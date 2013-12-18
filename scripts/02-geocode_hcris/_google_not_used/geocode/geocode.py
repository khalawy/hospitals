#from pygeocoder import Geocoder
from googlegeocoder import GoogleGeocoder

import csv, time

addrfile = open('addr.csv', 'r')
stop_time_for_geocoder = 35 # old 0.25

reader = csv.reader(addrfile)
allRows = [row for row in reader]
geocoder = GoogleGeocoder()

for address in allRows:

	try:
		search  = geocoder.get(str(address)[1:-1])
		print search[0].formatted_address + "^" + str(search[0].geometry.location) + "^" + str(search[0].geometry.location_type)

	except:
		print "bad address"

	time.sleep(stop_time_for_geocoder)
