# importing geopy library
from geopy.geocoders import Nominatim

import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

# calling the Nominatim tool
loc = Nominatim(user_agent="Behavioral biometric auth")

# entering the location name
getLoc = loc.geocode()

# printing address
print(getLoc.address)

def printing_lat_lom():
    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude,)
    print("Longitude = ", getLoc.longitude)


