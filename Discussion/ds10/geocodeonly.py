import tkinter
import math
import ssl
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json

# Put your API key between the quotes in the string below
GOOGLEAPIKEY = "Go get key"
geoDict = {}


# Given a string representing a location, return 2-element tuple
# (latitude, longitude) for that location 
#
# See https://developers.google.com/maps/documentation/geocoding/
# for details
#
def geocodeAddress(addressString):
   global geoURL
   global jsonResult, geoDict
   if addressString in geoDict:
      return geoDict[addressString]
   urlbase = "https://maps.googleapis.com/maps/api/geocode/json?address="
   geoURL = urlbase + quote_plus(addressString)
   geoURL = geoURL + "&key=" + GOOGLEAPIKEY

   ctx = ssl.create_default_context()
   ctx.check_hostname = False
   ctx.verify_mode = ssl.CERT_NONE
   
   stringResultFromGoogle = urlopen(geoURL, context=ctx).read().decode('utf8')
   jsonResult = json.loads(stringResultFromGoogle)
   if (jsonResult['status'] != "OK"):
      print("Status returned from Google geocoder *not* OK: {}".format(jsonResult['status']))
      result = (0.0, 0.0) # this prevents crash in retrieveMapFromGoogle - yields maps with lat/lon center at 0.0, 0.0
   else:
      loc = jsonResult['results'][0]['geometry']['location']
      result = (float(loc['lat']),float(loc['lng']))
   geoDict[addressString] = result
   return result

def testGeocode(numLoops = 1):
   queryList = ['New York, NY', 'Paris, France', 'Zihuatanejo, Mexico', 'Hue, Vietnam', 'Datong, China', 'Tokyo, Japan',
               'Berlin, Germany', 'Lima, Peru', 'Varanasi, India', 'Leighton Buzzard, England']
   for i in range(numLoops):
      for address in queryList:
         print(address, geocodeAddress(address))

# If file 'geodict.json' exists in the current folder,
# reads the JSON-formatted geocoding information from the file
# and "loads" it into a Python dictionary, geoDict.
# 
# If 'geodict.json' does not already exist, geoDict is set
# to an empty dictionary.

# 
def readGeoDict():
   global geoDict
   try:
      dictInFile = open('geodict.json')
   except:
      dictInFile = None
   if dictInFile != None:
      jsonString = dictInFile.read()
      geoDict = json.loads(jsonString)
      dictInFile.close()
   else:
      geoDict = {}

# Converts the dictionary with saved geocode information, geoDict,
# into JSON format and writes it to file 'geodict.json'
# 
def saveGeoDict():
   global jsonString
   print('saving geodict.json')
   dictOutFile = open('geodict.json', 'w')
   jsonString = json.dumps(geoDict)
   dictOutFile.write(jsonString)
   dictOutFile.close()


