import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim

#certificates
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

# calling the Nominatim tool
loc = Nominatim(user_agent="Behavioral biometric auth")

ip = input("Enter ip address: ")
res = DbIpCity.get(ip, api_key="free")
print(f"IP Address: {res.ip_address}")
print(f"Location: {res.city}, {res.region}, {res.country}")

# entering the location name
getLoc = loc.geocode(res.city)

print("Latitude = ", getLoc.latitude)
print("Longitude = ", getLoc.longitude)



