# import requests

# def fetch_weather_data(api_key, lat, lon):
#     url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
#     response = requests.get(url)
#     return response.json()

# # Example usage
# api_key = "9032df887a070c6d2773ddfdfd431d7c"
# lat, lon = 40.7128, -74.006  # NYC coordinates
# weather_data = fetch_weather_data(api_key, lat, lon)
# print(weather_data)

# import folium

# def create_base_map(center=[40.7128, -74.006], zoom_start=10):
#     return folium.Map(location=center, zoom_start=zoom_start, tiles="OpenStreetMap")

# # Example usage
# m = create_base_map()
# m.save("base_map.html")

# def add_weather_markers(map_obj, weather_data):
#     lat, lon = weather_data["coord"]["lat"], weather_data["coord"]["lon"]
#     temp = weather_data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
#     wind_speed = weather_data["wind"]["speed"]
#     popup = f"Temp: {temp:.2f}°C<br>Wind Speed: {wind_speed} m/s"
#     folium.Marker([lat, lon], popup=popup, icon=folium.Icon(color="blue")).add_to(map_obj)

# # Example usage
# add_weather_markers(m, weather_data)
# m.save("weather_map.html")

# import plotly.graph_objects as go

# def plot_wind_data(weather_data):
#     wind_speed = weather_data["wind"]["speed"]
#     wind_deg = weather_data["wind"]["deg"]
#     fig = go.Figure(go.Scatterpolar(
#         r=[wind_speed],
#         theta=[wind_deg],
#         fill="toself",
#         name="Wind Speed"
#     ))
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(visible=True, range=[0, 20]),
#             angularaxis=dict(rotation=90, direction="clockwise")
#         ),
#         showlegend=True
#     )
#     fig.show()

# # Example usage
# plot_wind_data(weather_data)

# from dash import Dash, html, dcc
# import dash_bootstrap_components as dbc

# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = html.Div([
#     html.H1("Weather Map"),
#     html.Iframe(id="map", srcDoc=open("weather_map.html", "r").read(), width="100%", height="600px")
# ])

# if __name__ == "__main__":
#     app.run_server(debug=True)

# import requests

# def fetch_windy_data(api_key, lat, lon, product="wind"):
#     url = "https://api.windy.com/api/point-forecast/v2"
#     params = {
#         "lat": lat,
#         "lon": lon,
#         "model": "gfs",
#         "parameters": [product],
#         "key": api_key,
#         "levels": "surface"
#     }
#     response = requests.get(url, params=params)
    
#     # Debug: Print the raw response
#     print("Status Code:", response.status_code)
#     print("Response Text:", response.text)
    
#     try:
#         return response.json()
#     except requests.exceptions.JSONDecodeError:
#         raise ValueError(f"API returned non-JSON response: {response.text}")

# # Example usage
# api_key = "FsWPqqP1ueoCxt0daZaanpGewgAYev4y"
# lat, lon = 40.7128, -74.006  # NYC coordinates
# wind_data = fetch_windy_data(api_key, lat, lon, product="wind")
# print(wind_data)

# import folium

# # Create a base map
# m = folium.Map(location=[40.7128, -74.006], zoom_start=5)

# # Add Windy's wind layer
# windy_tile_url = (
#     "https://tile.windy.com/tiles/windy/webcams_global/"
#     "{z}/{x}/{y}/2023112615/1800_1300.jpg?key=FsWPqqP1ueoCxt0daZaanpGewgAYev4y"
# )
# folium.TileLayer(
#     tiles=windy_tile_url,
#     attr="Windy",
#     name="Wind Layer",
#     overlay=True,
#     control=True
# ).add_to(m)

# # Add other layers (temperature, precipitation) similarly
# m.save("windy_map.html")

# from folium.plugins import HeatMap

# # Fetch wind data (speed and direction)
# wind_speeds = [point['wind_speed'] for point in wind_data['data']]
# coordinates = [[point['lat'], point['lon']] for point in wind_data['data']]

# # Create a heatmap for wind speed
# heatmap = HeatMap(
#     data=[[lat, lon, speed] for (lat, lon), speed in zip(coordinates, wind_speeds)],
#     name="Wind Speed",
#     radius=15,
#     blur=10,
#     min_opacity=0.5
# )
# heatmap.add_to(m)

# # Add layer control
# folium.LayerControl().add_to(m)
# m.save("custom_windy_map.html")

# import plotly.express as px

# # Example: Plot wind vectors with Plotly
# fig = px.scatter_mapbox(
#     wind_data,
#     lat="lat",
#     lon="lon",
#     size="wind_speed",
#     color="wind_speed",
#     hover_name="wind_direction",
#     mapbox_style="carto-positron",
#     title="Wind Speed and Direction"
# )
# fig.show()


# from flask import Flask, render_template
# import os

# app = Flask(__name__)

# # Create the templates and static directories
# if not os.path.exists('templates'):
#     os.makedirs('templates')
# if not os.path.exists('static'):
#     os.makedirs('static')

# # Create the HTML template
# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     # Write the HTML template
#     with open('templates/index.html', 'w') as f:
#         f.write('''
# <!DOCTYPE html>
# <html>
#     <head>
#         <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
#         <title>Weather Map</title>
#         <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
#         <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
#         <style>
#             #windy {
#                 width: 100%;
#                 height: 600px;
#             }
#         </style>
#     </head>
#     <body>
#         <div id="windy"></div>
#         <script src="{{ url_for('static', filename='script.js') }}"></script>
#     </body>
# </html>
# ''')

#     # Write the JavaScript file
#     with open('static/script.js', 'w') as f:
#         f.write('''
# const options = {
#     key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y', // REPLACE WITH YOUR KEY !!!
#     verbose: true
# };

# windyInit(options, windyAPI => {
#     const { overlays, broadcast } = windyAPI;

#     const windMetric = overlays.wind.metric;
#     console.log(windMetric);

#     overlays.wind.listMetrics();

#     overlays.wind.setMetric('bft');

#     broadcast.on('metricChanged', (overlay, newMetric) => {
#         console.log(overlay, newMetric);
#     });
# });
# ''')

#     # Run the application
#     app.run(debug=True)


# from flask import Flask, render_template
# import os

# app = Flask(__name__)

# # Create the templates and static directories
# if not os.path.exists('templates'):
#     os.makedirs('templates')
# if not os.path.exists('static'):
#     os.makedirs('static')

# # Create the HTML template
# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     # Write the HTML template
#     with open('templates/index.html', 'w') as f:
#         f.write('''
# <!DOCTYPE html>
# <html>
#     <head>
#         <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
#         <title>Weather Map</title>
#         <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
#         <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
#         <style>
#             body {
#                 margin: 0;
#                 padding: 0;
#                 display: flex;
#                 height: 100vh;
#             }
#             #windy {
#                 width: 50%;
#                 height: 100vh;
#             }
#             #content {
#                 width: 50%;
#                 padding: 20px;
#             }
#         </style>
#     </head>
#     <body>
#         <div id="windy"></div>
#         <div id="content">
#             <!-- Your other content can go here -->
#         </div>
#         <script src="{{ url_for('static', filename='script.js') }}"></script>
#     </body>
# </html>
# ''')

#     # Write the JavaScript file
#     with open('static/script.js', 'w') as f:
#         f.write('''
# const options = {
#     key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y', // REPLACE WITH YOUR KEY !!!
#     verbose: true
# };

# windyInit(options, windyAPI => {
#     const { overlays, broadcast } = windyAPI;
#     const windMetric = overlays.wind.metric;
#     console.log(windMetric);
#     overlays.wind.listMetrics();
#     overlays.wind.setMetric('bft');
#     broadcast.on('metricChanged', (overlay, newMetric) => {
#         console.log(overlay, newMetric);
#     });
# });
# ''')

#     # Run the application
#     app.run(debug=True)

# OPEN_CAGE_GEOCODING_API = cb40be970fa24926b3b0cb4233b21f1e


# import streamlit as st
# import streamlit.components.v1 as components

# def main():
#     # Set page config to wide mode
#     st.set_page_config(layout="wide")
    
#     # Create two columns
#     col1, col2 = st.columns(2)
    
#     with col1:
#         # Create custom HTML/JS component for Windy map
#         components.html("""
#             <!DOCTYPE html>
#             <html>
#                 <head>
#                     <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
#                     <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
#                     <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
#                     <style>
#                         #windy {
#                             width: 100%;
#                             height: 600px;
#                             border-radius: 10px;
#                         }
#                     </style>
#                 </head>
#                 <body>
#                     <div id="windy"></div>
#                     <script>
#                         const options = {
#                             key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y', // REPLACE WITH YOUR KEY !!!
#                             verbose: true
#                         };

#                         windyInit(options, windyAPI => {
#                             const { overlays, broadcast } = windyAPI;
#                             const windMetric = overlays.wind.metric;
#                             console.log(windMetric);
#                             overlays.wind.listMetrics();
#                             overlays.wind.setMetric('bft');
#                             broadcast.on('metricChanged', (overlay, newMetric) => {
#                                 console.log(overlay, newMetric);
#                             });
#                         });
#                     </script>
#                 </body>
#             </html>
#         """, height=600)
    
#     with col2:
#         # Add your weather information and controls here
#         st.title("Weather Dashboard")
#         st.write("Add your weather information and controls in this column")
        
#         # Example controls
#         if st.button("Refresh Data"):
#             st.write("Refreshing weather data...")
            
#         metric = st.selectbox(
#             "Wind Speed Unit",
#             ["bft", "kt", "m/s", "km/h", "mph"]
#         )
        
#         # Add more weather information widgets as needed

# if __name__ == "__main__":
#     main()


import streamlit as st
import streamlit.components.v1 as components
import requests
from datetime import datetime
import pandas as pd

def get_coordinates(city):
    """Get latitude and longitude for a given city using OpenCage Geocoding API"""
    api_key = "cb40be970fa24926b3b0cb4233b21f1e"  # Replace with your OpenCage API key
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    
    params = {
        'q': city,
        'key': api_key,
        'limit': 1
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data['results']:
            lat = data['results'][0]['geometry']['lat']
            lng = data['results'][0]['geometry']['lng']
            return lat, lng
        return None, None
    except Exception as e:
        st.error(f"Error getting coordinates: {str(e)}")
        return None, None

def get_weather_data(lat, lon):
    """Get weather data from OpenWeatherMap API"""
    api_key = "a37be5e437c1d804ad68daaec7139c6c" 
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        st.error(f"Error getting weather data: {str(e)}")
        return None

def main():
    st.set_page_config(layout="wide", page_title="Weather Dashboard")
    
    # Title and description
    st.title("🌤️ Weather Dashboard")
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        # City selection
        cities_df = pd.read_csv('https://raw.githubusercontent.com/datasets/world-cities/master/data/world-cities.csv')
        all_cities = sorted(cities_df['name'].unique())
        
        selected_city = st.selectbox(
            "Select a city",
            all_cities,
            index=all_cities.index("London") if "London" in all_cities else 0
        )
        
        # Get coordinates for selected city
        lat, lng = get_coordinates(selected_city)
        
        if lat and lng:
            # Create custom HTML/JS component for Windy map
            components.html(f"""
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
                        <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
                        <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
                        <style>
                            #windy {{
                                width: 100%;
                                height: 600px;
                                border-radius: 10px;
                            }}
                        </style>
                    </head>
                    <body>
                        <div id="windy"></div>
                        <script>
                            const options = {{
                                key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y',
                                verbose: true,
                                lat: {lat},
                                lon: {lng},
                                zoom: 8
                            }};

                            windyInit(options, windyAPI => {{
                                const {{ overlays, broadcast }} = windyAPI;
                                const windMetric = overlays.wind.metric;
                                overlays.wind.setMetric('bft');
                            }});
                        </script>
                    </body>
                </html>
            """, height=600)
    
    with col2:
        if lat and lng:
            weather_data = get_weather_data(lat, lng)
            
            if weather_data:
                # Display current weather information
                st.subheader(f"Current Weather in {selected_city}")
                
                # Create three columns for weather metrics
                metric_col1, metric_col2, metric_col3 = st.columns(3)
                
                with metric_col1:
                    st.metric(
                        "Temperature",
                        f"{weather_data['main']['temp']}°C",
                        f"{weather_data['main']['temp_max'] - weather_data['main']['temp_min']:+.1f}°C"
                    )
                
                with metric_col2:
                    st.metric(
                        "Humidity",
                        f"{weather_data['main']['humidity']}%"
                    )
                
                with metric_col3:
                    st.metric(
                        "Wind Speed",
                        f"{weather_data['wind']['speed']} m/s"
                    )
                
                # Weather description and icon
                weather_icon_code = weather_data['weather'][0]['icon']
                weather_icon_url = f"http://openweathermap.org/img/w/{weather_icon_code}.png"
                st.image(weather_icon_url, width=100)
                st.write(f"**Condition:** {weather_data['weather'][0]['description'].title()}")
                
                # Pressure
                st.write(f"**Pressure:** {weather_data['main']['pressure']} hPa")
                
                # Sunrise and sunset times
                sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'])
                sunset = datetime.fromtimestamp(weather_data['sys']['sunset'])
                st.write(f"**Sunrise:** {sunrise.strftime('%H:%M')} local time")
                st.write(f"**Sunset:** {sunset.strftime('%H:%M')} local time")
                
                # Weather Video Generation
                st.subheader("Weather Video Generation")
                if st.button("Generate Weather Video"):
                    # Here you would typically call a service to generate a weather video
                    # For now, we'll just show a placeholder message
                    st.info("Generating weather video... This feature requires integration with a video generation service.")
                    
                    # Placeholder for video display
                    st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
                
                # Additional controls
                st.subheader("Map Controls")
                metric = st.selectbox(
                    "Wind Speed Unit",
                    ["bft", "kt", "m/s", "km/h", "mph"]
                )
                
                # Forecast period selector
                forecast_period = st.slider(
                    "Forecast Period (hours)",
                    0, 72, 24,
                    step=6
                )

if __name__ == "__main__":
    main()