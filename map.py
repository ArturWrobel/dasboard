import folium
import os
import json

m = folium.Map(location = [52.231702816483164, 21.006224155426025], zoom_start = 13)

tooltip = "Click for Info"

logo = folium.features.CustomIcon("orange.jpg", icon_size = (30,30))

folium.Marker([52.231702816483164, 21.006224155426025],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([52.218098581239495, 20.962386131286618],
              popup='<strong>Dworzec Zachodni</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([52.21306330038455, 20.95112085342407],
              popup='<strong>Reduta</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([52.2126557200447, 20.95571279525757],
              popup='<strong>Blue City</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),
folium.Marker([52.208431784250855, 20.94619631767273],
              popup='<strong>Orange Polska S.A.</strong>',
              tooltip=tooltip,
              icon=logo).add_to(m),


#woj = os.path.join('', 'woj.json')

#folium.GeoJson("", name='wojewodztwa').add_to(m)

m.save("map.html")