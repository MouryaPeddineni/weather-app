# import folium

# # Your Windy API Key (replace with your actual API key)
# WINDY_API_KEY = "FsWPqqP1ueoCxt0daZaanpGewgAYev4y"

# # Center map on New York City
# m = folium.Map(location=[40.7128, -74.0060], zoom_start=7)

# # JavaScript to add Windy animation
# windy_script = f"""
#     <script>
#         var windyInit = function (options) {{
#             var {{"key": "{WINDY_API_KEY}", "lat": 40.7128, "lon": -74.0060, "zoom": 7 }};
#             windyty.init(options, function () {{
#                 var map = windyAPI.map;
#                 L.popup()
#                     .setLatLng([40.7128, -74.0060])
#                     .setContent("Windy animation active")
#                     .openOn(map);
#             }});
#         }};
#     </script>
#     <script async src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
# """

# # Add Windy animation to the Folium map using an HTML iframe overlay
# m.get_root().html.add_child(folium.Element(windy_script))

# # Save and display the map
# m.save("windy_nyc_map.html")
# m


import requests

# Define your API key and endpoint
api_key = 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y'
url = 'https://api.windy.com/api/point-forecast/v2'

# Set the parameters for the request
params = {
    "lat": 49.809,  # Replace with your desired latitude
    "lon": 16.787,  # Replace with your desired longitude
    "model": "gfs",
    "parameters": ["wind", "dewpoint", "rh", "pressure"],
    "levels": ["surface", "800h", "300h"],
    "key": api_key
}

# Make the API request
response = requests.post(url, json=params)

# Check if the request was successful
if response.status_code == 200:
    weather_data = response.json()
else:
    print("Error fetching data:", response.status_code)

import folium

# Create a map centered at the specified location
map_center = [49.809, 16.787]  # Replace with your desired coordinates
windy_map = folium.Map(location=map_center, zoom_start=8)

# Add a marker for the location
folium.Marker(location=map_center, popup='Weather Data').add_to(windy_map)

# Save the map to an HTML file
windy_map.save('windy_map.html')