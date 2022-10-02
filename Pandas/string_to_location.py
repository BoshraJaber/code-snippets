from geopy.geocoders import Nominatim

# Example Geocoding Addresses with Pandas and Geopy
# Convert a string to location
# dir(geopy)

nom = Nominatim(user_agent="first_botebook.ipynb")
location = nom.geocode("175 5th Avenue NYC")
print(location)
location.longitude
type(location)