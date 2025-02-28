import folium
from folium import plugins
import numpy as np
import pandas as pd
import requests
from datetime import datetime
import json
from branca.colormap import LinearColormap
import xarray as xr

class WeatherMap:
    def __init__(self, center_lat=0, center_lng=0, zoom_start=3):
        """Initialize the weather map with base settings."""
        self.map = folium.Map(
            location=[center_lat, center_lng],
            zoom_start=zoom_start,
            tiles='cartodbpositron'
        )
        
        # Add layer control
        self.layer_control = folium.LayerControl()
        self.map.add_child(self.layer_control)
        
    def add_temperature_layer(self, temp_data):
        """
        Add temperature layer to map.
        temp_data: DataFrame with columns [lat, lon, temperature]
        """
        # Create color map for temperature
        colormap = LinearColormap(
            colors=['blue', 'yellow', 'red'],
            vmin=temp_data['temperature'].min(),
            vmax=temp_data['temperature'].max()
        )
        
        # Create temperature layer
        temp_layer = folium.FeatureGroup(name='Temperature')
        
        for _, row in temp_data.iterrows():
            folium.CircleMarker(
                location=[row['lat'], row['lon']],
                radius=15,
                color=None,
                fill=True,
                fillColor=colormap(row['temperature']),
                fillOpacity=0.7,
                popup=f"{row['temperature']}°C"
            ).add_to(temp_layer)
        
        temp_layer.add_to(self.map)
        colormap.add_to(self.map)
        
    def add_wind_layer(self, wind_data):
        """
        Add wind layer with arrows showing direction and speed.
        wind_data: DataFrame with columns [lat, lon, speed, direction]
        """
        wind_layer = folium.FeatureGroup(name='Wind')
        
        # Create wind marker cluster
        wind_markers = plugins.MarkerCluster()
        
        for _, row in wind_data.iterrows():
            # Convert wind direction to arrow rotation
            rotation = row['direction']
            
            # Create arrow icon
            arrow_icon = plugins.BeautifyIcon(
                icon='arrow-up',
                border_color='transparent',
                text_color='black',
                icon_shape='circle',
                rotate=rotation
            )
            
            # Add marker with arrow
            folium.Marker(
                location=[row['lat'], row['lon']],
                icon=arrow_icon,
                popup=f"Wind Speed: {row['speed']} m/s"
            ).add_to(wind_markers)
        
        wind_markers.add_to(wind_layer)
        wind_layer.add_to(self.map)
        
    def add_precipitation_layer(self, precip_data):
        """
        Add precipitation layer with radar-like visualization.
        precip_data: DataFrame with columns [lat, lon, precipitation]
        """
        precip_layer = folium.FeatureGroup(name='Precipitation')
        
        # Create precipitation color map
        precip_colors = ['#FFFFFF', '#A6F28F', '#3DBA3D', '#2B8CBE', '#084594']
        precip_colormap = LinearColormap(
            colors=precip_colors,
            vmin=precip_data['precipitation'].min(),
            vmax=precip_data['precipitation'].max()
        )
        
        for _, row in precip_data.iterrows():
            folium.CircleMarker(
                location=[row['lat'], row['lon']],
                radius=20,
                color=None,
                fill=True,
                fillColor=precip_colormap(row['precipitation']),
                fillOpacity=0.5,
                popup=f"{row['precipitation']} mm"
            ).add_to(precip_layer)
        
        precip_layer.add_to(self.map)
        precip_colormap.add_to(self.map)
    
    def add_pressure_layer(self, pressure_data):
        """
        Add pressure contours layer.
        pressure_data: DataFrame with columns [lat, lon, pressure]
        """
        pressure_layer = folium.FeatureGroup(name='Pressure')
        
        # Create pressure contours
        locations = pressure_data[['lat', 'lon', 'pressure']].values
        
        # Add isolines
        plugins.Iso().add_to(pressure_layer)
        pressure_layer.add_to(self.map)

    def add_custom_legend(self):
        """Add a custom legend to the map."""
        legend_html = """
        <div style="position: fixed; bottom: 50px; right: 50px; z-index: 1000; background-color: white; padding: 10px; border-radius: 5px;">
            <h4>Weather Conditions</h4>
            <div id="legend-content">
                <div class="legend-item">
                    <span style="background-color: red; width: 20px; height: 20px; display: inline-block;"></span>
                    <span>High Temperature</span>
                </div>
                <div class="legend-item">
                    <span style="background-color: blue; width: 20px; height: 20px; display: inline-block;"></span>
                    <span>Low Temperature</span>
                </div>
                <div class="legend-item">
                    <i class="fa fa-arrow-up"></i>
                    <span>Wind Direction</span>
                </div>
            </div>
        </div>
        """
        self.map.get_root().html.add_child(folium.Element(legend_html))

    def generate_sample_data(self, n_points=100):
        """Generate sample weather data for testing."""
        lats = np.random.uniform(-80, 80, n_points)
        lons = np.random.uniform(-180, 180, n_points)
        
        # Temperature data
        temps = np.random.uniform(-10, 40, n_points)
        temp_data = pd.DataFrame({
            'lat': lats,
            'lon': lons,
            'temperature': temps
        })
        
        # Wind data
        wind_speeds = np.random.uniform(0, 20, n_points)
        wind_directions = np.random.uniform(0, 360, n_points)
        wind_data = pd.DataFrame({
            'lat': lats,
            'lon': lons,
            'speed': wind_speeds,
            'direction': wind_directions
        })
        
        # Precipitation data
        precip = np.random.uniform(0, 50, n_points)
        precip_data = pd.DataFrame({
            'lat': lats,
            'lon': lons,
            'precipitation': precip
        })
        
        return temp_data, wind_data, precip_data

# Example usage
if __name__ == "__main__":
    # Create weather map centered on Europe
    weather_map = WeatherMap(center_lat=48.8566, center_lng=2.3522, zoom_start=5)
    
    # Generate sample data
    temp_data, wind_data, precip_data = weather_map.generate_sample_data()
    
    # Add layers
    weather_map.add_temperature_layer(temp_data)
    weather_map.add_wind_layer(wind_data)
    weather_map.add_precipitation_layer(precip_data)
    weather_map.add_custom_legend()
    
    # Save the map
    weather_map.map.save('weather_map.html')
