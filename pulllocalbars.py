from geopy.geocoders import Nominatim
import requests

geolocator = Nominatim(user_agent="locatunes")
location = geolocator.geocode("880 New jersey ave se")
print(location.address)
print((location.latitude, location.longitude))


local = requests.get(   "http://api.touchtunes.com/v2/locations?user_latitude={}"
                        "&user_longitude={}"
                        "&latitude={}"
                        "&longitude={}&radius=10".format(location.latitude,location.longitude,location.latitude,location.longitude))
print (local)