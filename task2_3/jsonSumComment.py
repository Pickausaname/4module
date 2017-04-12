import json
import urllib

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'http://python-data.dr-chuck.net/comments_283750.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
info = json.loads(data)
results=0
for i in range(len(info['comments'])):
    results+=info['comments'][i]['count']

print results


