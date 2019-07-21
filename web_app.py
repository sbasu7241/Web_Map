import folium
import pandas

data = pandas.read_csv("countries.csv")
lat = list(data["lat"])
lon = list(data["lng"])
pop = list(data["population"])
city = list(data["city"])

def color_producer(elevation):
    if elevation < 500000:
        return 'green'
    elif 500000 <= elevation < 1000000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[23.892126, 78.115779], zoom_start=6)

fgv = folium.FeatureGroup(name="Cities")

for lt, ln, cty, popul in zip(lat, lon, city, pop):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=6,popup=cty,fill_color=color_producer(popul),color='grey',fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('india_state.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'blue' if ord(x['properties']['NAME_1'][0]) < 72
else 'orange' if 72 <= ord(x['properties']['NAME_1'][0]) < 81 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("Map.html")
