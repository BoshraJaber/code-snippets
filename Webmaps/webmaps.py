import folium

# 1. create a map object:
# print(dir(folium))
map = folium.Map(location=[80, -100], zoom_start=10, tiles="Mapbox Bright")

# 2. convert map object to js,css,html code
map.save("index.html")