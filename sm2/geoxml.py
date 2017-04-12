import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)

    #TODO
    #Return lat,lng,adress

    print 'lat: ',tree.find('result/geometry/location/lat').text
    print 'lng: ',tree.find('result/geometry/location/lng').text
    print 'location: ',tree.find('result/formatted_address').text

