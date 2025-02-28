# # import folium
# # from folium import plugins
# # import numpy as np
# # import requests
# # import json
# # from datetime import datetime
# # import pandas as pd

# # class WindyMapReplica:
# #     def __init__(self):
# #         self.custom_css = """
# #         <style>
# #             /* Wind particle animation */
# #             @keyframes particleMove {
# #                 0% { transform: translate(0, 0); }
# #                 100% { transform: translate(100px, 100px); }
# #             }
            
# #             .wind-particle {
# #                 position: absolute;
# #                 width: 2px;
# #                 height: 2px;
# #                 background: rgba(255, 255, 255, 0.8);
# #                 border-radius: 50%;
# #             }
            
# #             /* Temperature gradient overlay */
# #             .temp-overlay {
# #                 position: absolute;
# #                 width: 100%;
# #                 height: 100%;
# #                 background: linear-gradient(
# #                     to right,
# #                     rgba(0, 0, 255, 0.2),
# #                     rgba(255, 0, 0, 0.2)
# #                 );
# #                 mix-blend-mode: multiply;
# #             }
            
# #             /* Weather layer controls */
# #             .layer-control {
# #                 position: fixed;
# #                 top: 20px;
# #                 right: 20px;
# #                 background: rgba(255, 255, 255, 0.9);
# #                 padding: 10px;
# #                 border-radius: 5px;
# #                 z-index: 1000;
# #             }
            
# #             /* Animation controls */
# #             .animation-control {
# #                 position: fixed;
# #                 bottom: 20px;
# #                 left: 50%;
# #                 transform: translateX(-50%);
# #                 background: rgba(0, 0, 0, 0.7);
# #                 padding: 10px;
# #                 border-radius: 5px;
# #                 color: white;
# #                 z-index: 1000;
# #             }
# #         </style>
# #         """
        
# #         self.custom_js = """
# #         <script>
# #         // Wind particle system
# #         function createWindParticles() {
# #             const container = document.createElement('div');
# #             container.style.position = 'absolute';
# #             container.style.width = '100%';
# #             container.style.height = '100%';
# #             container.style.pointerEvents = 'none';
            
# #             for (let i = 0; i < 1000; i++) {
# #                 const particle = document.createElement('div');
# #                 particle.className = 'wind-particle';
# #                 particle.style.left = Math.random() * 100 + '%';
# #                 particle.style.top = Math.random() * 100 + '%';
# #                 container.appendChild(particle);
# #             }
            
# #             document.querySelector('#map').appendChild(container);
# #         }
        
# #         // Initialize animation system
# #         document.addEventListener('DOMContentLoaded', function() {
# #             createWindParticles();
            
# #             // Add animation controls
# #             const controls = document.createElement('div');
# #             controls.className = 'animation-control';
# #             controls.innerHTML = `
# #                 <button onclick="toggleAnimation()">Play/Pause</button>
# #                 <input type="range" min="0" max="24" value="0" onchange="updateTimeStep(this.value)">
# #                 <span id="time-display">00:00</span>
# #             `;
# #             document.body.appendChild(controls);
# #         });
        
# #         function toggleAnimation() {
# #             // Animation toggle logic
# #         }
        
# #         function updateTimeStep(value) {
# #             document.getElementById('time-display').textContent = 
# #                 String(value).padStart(2, '0') + ':00';
# #         }
# #         </script>
# #         """

# #     def create_map(self, center_lat=10.741, center_lng=68.634, zoom_start=4):
# #         """Create the base map with all necessary layers."""
# #         # Create base map
# #         m = folium.Map(
# #             location=[center_lat, center_lng],
# #             zoom_start=zoom_start,
# #             tiles='cartodbdark_matter',  # Dark theme similar to Windy
# #             attr='CartoDB Dark Matter'
# #         )
        
# #         # Add custom CSS and JS
# #         m.get_root().header.add_child(folium.Element(self.custom_css))
# #         m.get_root().script.add_child(folium.Element(self.custom_js))
        
# #         # Add wind layer (using flow layer plugin)
# #         wind_data = self._generate_sample_wind_data(center_lat, center_lng)
# #         plugins.VectorFieldOverlay(
# #             wind_data,
# #             alpha=0.5,
# #             color='white',
# #             name='wind_layer'
# #         ).add_to(m)
        
# #         # Add temperature layer
# #         temp_data = self._generate_sample_temp_data(center_lat, center_lng)
# #         plugins.HeatMap(
# #             temp_data,
# #             name='temperature_layer',
# #             min_opacity=0.3,
# #             max_opacity=0.7,
# #             radius=25
# #         ).add_to(m)
        
# #         # Add layer control
# #         folium.LayerControl(position='topright').add_to(m)
        
# #         # Add custom controls HTML
# #         self._add_custom_controls(m)
        
# #         return m

# #     def _generate_sample_wind_data(self, center_lat, center_lng):
# #         """Generate sample wind vector data."""
# #         lat_span = 20
# #         lon_span = 20
# #         grid_size = 30
        
# #         lats = np.linspace(center_lat - lat_span, center_lat + lat_span, grid_size)
# #         lons = np.linspace(center_lng - lon_span, center_lng + lon_span, grid_size)
        
# #         data = []
# #         for lat in lats:
# #             for lon in lons:
# #                 # Generate sample wind vectors
# #                 u = np.sin(lat/10) * np.cos(lon/10)  # East-West component
# #                 v = np.cos(lat/10) * np.sin(lon/10)  # North-South component
# #                 data.append([lat, lon, u, v])
        
# #         return data

# #     def _generate_sample_temp_data(self, center_lat, center_lng):
# #         """Generate sample temperature data."""
# #         lat_span = 20
# #         lon_span = 20
# #         grid_size = 50
        
# #         lats = np.linspace(center_lat - lat_span, center_lat + lat_span, grid_size)
# #         lons = np.linspace(center_lng - lon_span, center_lng + lon_span, grid_size)
        
# #         data = []
# #         for lat in lats:
# #             for lon in lons:
# #                 # Generate sample temperature values
# #                 temp = 20 + 10 * np.sin(lat/10) * np.cos(lon/10)
# #                 weight = abs(temp) / 40  # Normalize for heatmap
# #                 data.append([lat, lon, weight])
        
# #         return data

# #     def _add_custom_controls(self, m):
# #         """Add custom control elements to the map."""
# #         controls_html = """
# #         <div class="layer-control">
# #             <div style="margin-bottom: 10px;">
# #                 <strong>Weather Layers</strong>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="wind" checked>
# #                 <label for="wind">Wind</label>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="temp" checked>
# #                 <label for="temp">Temperature</label>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="pressure">
# #                 <label for="pressure">Pressure</label>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="clouds">
# #                 <label for="clouds">Clouds</label>
# #             </div>
# #         </div>
# #         """
# #         m.get_root().html.add_child(folium.Element(controls_html))

# # def main():
# #     # Create map instance
# #     windy_map = WindyMapReplica()
    
# #     # Generate map
# #     m = windy_map.create_map()
    
# #     # Save to HTML file
# #     m.save('windy_replica.html')

# # if __name__ == "__main__":
# #     main()

# # import folium
# # from folium import plugins
# # import numpy as np
# # from datetime import datetime

# # class WindyMapReplica:
# #     def __init__(self):
# #         self.custom_css = """
# #         <style>
# #             /* Wind particle animation */
# #             @keyframes particleMove {
# #                 0% { transform: translate(0, 0); }
# #                 100% { transform: translate(100px, 100px); }
# #             }
            
# #             .wind-particle {
# #                 position: absolute;
# #                 width: 2px;
# #                 height: 2px;
# #                 background: rgba(255, 255, 255, 0.8);
# #                 border-radius: 50%;
# #             }
            
# #             /* Temperature gradient overlay */
# #             .temp-overlay {
# #                 position: absolute;
# #                 width: 100%;
# #                 height: 100%;
# #                 background: linear-gradient(
# #                     to right,
# #                     rgba(0, 0, 255, 0.2),
# #                     rgba(255, 0, 0, 0.2)
# #                 );
# #                 mix-blend-mode: multiply;
# #             }
            
# #             /* Weather layer controls */
# #             .layer-control {
# #                 position: fixed;
# #                 top: 20px;
# #                 right: 20px;
# #                 background: rgba(255, 255, 255, 0.9);
# #                 padding: 10px;
# #                 border-radius: 5px;
# #                 z-index: 1000;
# #             }
# #         </style>
# #         """

# #     def create_map(self, center_lat=10.741, center_lng=68.634, zoom_start=4):
# #         """Create the base map with all necessary layers."""
# #         # Create base map
# #         m = folium.Map(
# #             location=[center_lat, center_lng],
# #             zoom_start=zoom_start,
# #             tiles='cartodbdark_matter',  # Dark theme similar to Windy
# #             attr='CartoDB Dark Matter'
# #         )
        
# #         # Add custom CSS
# #         m.get_root().header.add_child(folium.Element(self.custom_css))
        
# #         # Add wind layer using StreamLines
# #         wind_data = self._generate_sample_wind_data(center_lat, center_lng)
        
# #         plugins.StreamLines(
# #             wind_data,
# #             density=1,
# #             maxAge=200,
# #             velocityScale=0.2,
# #             color='white',
# #             name='wind_layer'
# #         ).add_to(m)
        
# #         # Add temperature layer
# #         temp_data = self._generate_sample_temp_data(center_lat, center_lng)
# #         plugins.HeatMap(
# #             temp_data,
# #             name='temperature_layer',
# #             min_opacity=0.3,
# #             max_opacity=0.7,
# #             radius=25
# #         ).add_to(m)
        
# #         # Add layer control
# #         folium.LayerControl(position='topright').add_to(m)
        
# #         # Add custom controls HTML
# #         self._add_custom_controls(m)
        
# #         return m

# #     def _generate_sample_wind_data(self, center_lat, center_lng):
# #         """Generate sample wind vector data."""
# #         lat_span = 20
# #         lon_span = 20
# #         grid_size = 30
        
# #         lats = np.linspace(center_lat - lat_span, center_lat + lat_span, grid_size)
# #         lons = np.linspace(center_lng - lon_span, center_lng + lon_span, grid_size)
        
# #         data = {
# #             'data': [],
# #             'headers': {
# #                 'dx': lon_span * 2 / grid_size,
# #                 'dy': lat_span * 2 / grid_size,
# #                 'la1': float(lats[0]),
# #                 'la2': float(lats[-1]),
# #                 'lo1': float(lons[0]),
# #                 'lo2': float(lons[-1]),
# #                 'nx': len(lons),
# #                 'ny': len(lats)
# #             }
# #         }
        
# #         for lat in lats:
# #             row = []
# #             for lon in lons:
# #                 # Generate sample wind vectors
# #                 u = np.sin(lat/10) * np.cos(lon/10) * 10  # East-West component
# #                 v = np.cos(lat/10) * np.sin(lon/10) * 10  # North-South component
# #                 row.append([u, v])
# #             data['data'].append(row)
        
# #         return data

# #     def _generate_sample_temp_data(self, center_lat, center_lng):
# #         """Generate sample temperature data."""
# #         lat_span = 20
# #         lon_span = 20
# #         grid_size = 50
        
# #         lats = np.linspace(center_lat - lat_span, center_lat + lat_span, grid_size)
# #         lons = np.linspace(center_lng - lon_span, center_lng + lon_span, grid_size)
        
# #         data = []
# #         for lat in lats:
# #             for lon in lons:
# #                 # Generate sample temperature values
# #                 temp = 20 + 10 * np.sin(lat/10) * np.cos(lon/10)
# #                 weight = abs(temp) / 40  # Normalize for heatmap
# #                 data.append([lat, lon, weight])
        
# #         return data

# #     def _add_custom_controls(self, m):
# #         """Add custom control elements to the map."""
# #         controls_html = """
# #         <div class="layer-control">
# #             <div style="margin-bottom: 10px;">
# #                 <strong>Weather Layers</strong>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="wind" checked>
# #                 <label for="wind">Wind</label>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="temp" checked>
# #                 <label for="temp">Temperature</label>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="pressure">
# #                 <label for="pressure">Pressure</label>
# #             </div>
# #             <div>
# #                 <input type="checkbox" id="clouds">
# #                 <label for="clouds">Clouds</label>
# #             </div>
# #         </div>
# #         """
# #         m.get_root().html.add_child(folium.Element(controls_html))

# # def main():
# #     # Create map instance
# #     windy_map = WindyMapReplica()
    
# #     # Generate map
# #     m = windy_map.create_map()
    
# #     # Save to HTML file
# #     m.save('windy_replica.html')

# # if __name__ == "__main__":
# #     main()


import folium
from folium import plugins
import numpy as np
from datetime import datetime

class WindyMapReplica:
    def __init__(self):
        self.custom_css = """
        <style>
            /* Wind particle animation */
            @keyframes particleMove {
                0% { transform: translate(0, 0); }
                100% { transform: translate(100px, 100px); }
            }
            
            .wind-particle {
                position: absolute;
                width: 2px;
                height: 2px;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 50%;
            }
            
            /* Temperature gradient overlay */
            .temp-overlay {
                position: absolute;
                width: 100%;
                height: 100%;
                background: linear-gradient(
                    to right,
                    rgba(0, 0, 255, 0.2),
                    rgba(255, 0, 0, 0.2)
                );
                mix-blend-mode: multiply;
            }
            
            /* Weather layer controls */
            .layer-control {
                position: fixed;
                top: 20px;
                right: 20px;
                background: rgba(255, 255, 255, 0.9);
                padding: 10px;
                border-radius: 5px;
                z-index: 1000;
            }
        </style>
        """

    def create_map(self, center_lat=10.741, center_lng=68.634, zoom_start=4):
        """Create the base map with all necessary layers."""
        # Create base map
        m = folium.Map(
            location=[center_lat, center_lng],
            zoom_start=zoom_start,
            tiles='cartodbdark_matter',
            attr='CartoDB Dark Matter'
        )
        
        # Add custom CSS
        m.get_root().header.add_child(folium.Element(self.custom_css))
        
        # Add wind layer using arrows
        wind_data = self._generate_sample_wind_data(center_lat, center_lng)
        self._add_wind_arrows(m, wind_data)
        
        # Add temperature layer
        temp_data = self._generate_sample_temp_data(center_lat, center_lng)
        plugins.HeatMap(
            temp_data,
            name='temperature_layer',
            min_opacity=0.3,
            max_opacity=0.7,
            radius=25
        ).add_to(m)
        
        # Add layer control
        folium.LayerControl(position='topright').add_to(m)
        
        # Add custom controls HTML
        self._add_custom_controls(m)
        
        return m

    def _add_wind_arrows(self, m, wind_data):
        """Add wind arrows to represent wind direction and speed."""
        feature_group = folium.FeatureGroup(name='wind_layer')
        
        lats = np.linspace(
            wind_data['headers']['la1'],
            wind_data['headers']['la2'],
            wind_data['headers']['ny']
        )
        lons = np.linspace(
            wind_data['headers']['lo1'],
            wind_data['headers']['lo2'],
            wind_data['headers']['nx']
        )
        
        # Add arrows for every nth point to avoid overcrowding
        n = 3
        for i in range(0, len(lats), n):
            for j in range(0, len(lons), n):
                u, v = wind_data['data'][i][j]
                
                # Calculate arrow angle and magnitude
                angle = np.arctan2(v, u) * 180 / np.pi
                magnitude = np.sqrt(u**2 + v**2)
                
                # Create arrow icon
                arrow = plugins.BeautifyIcon(
                    icon='arrow-up',
                    border_color='#ffffff',
                    text_color='#ffffff',
                    background_color='transparent',
                    inner_icon_style=f'transform: rotate({angle}deg);',
                    icon_shape='marker'
                )
                
                # Add marker with arrow icon
                folium.Marker(
                    location=[lats[i], lons[j]],
                    icon=arrow,
                    popup=f'Wind Speed: {magnitude:.1f} m/s\nDirection: {angle:.1f}°'
                ).add_to(feature_group)
        
        feature_group.add_to(m)

    def _generate_sample_wind_data(self, center_lat, center_lng):
        """Generate sample wind vector data."""
        lat_span = 20
        lon_span = 20
        grid_size = 30
        
        lats = np.linspace(center_lat - lat_span, center_lat + lat_span, grid_size)
        lons = np.linspace(center_lng - lon_span, center_lng + lon_span, grid_size)
        
        data = {
            'data': [],
            'headers': {
                'dx': lon_span * 2 / grid_size,
                'dy': lat_span * 2 / grid_size,
                'la1': float(lats[0]),
                'la2': float(lats[-1]),
                'lo1': float(lons[0]),
                'lo2': float(lons[-1]),
                'nx': len(lons),
                'ny': len(lats)
            }
        }
        
        for lat in lats:
            row = []
            for lon in lons:
                # Generate sample wind vectors
                u = np.sin(lat/10) * np.cos(lon/10) * 10  # East-West component
                v = np.cos(lat/10) * np.sin(lon/10) * 10  # North-South component
                row.append([u, v])
            data['data'].append(row)
        
        return data

    def _generate_sample_temp_data(self, center_lat, center_lng):
        """Generate sample temperature data."""
        lat_span = 20
        lon_span = 20
        grid_size = 50
        
        lats = np.linspace(center_lat - lat_span, center_lat + lat_span, grid_size)
        lons = np.linspace(center_lng - lon_span, center_lng + lon_span, grid_size)
        
        data = []
        for lat in lats:
            for lon in lons:
                # Generate sample temperature values
                temp = 20 + 10 * np.sin(lat/10) * np.cos(lon/10)
                weight = abs(temp) / 40  # Normalize for heatmap
                data.append([lat, lon, weight])
        
        return data

    def _add_custom_controls(self, m):
        """Add custom control elements to the map."""
        controls_html = """
        <div class="layer-control">
            <div style="margin-bottom: 10px;">
                <strong>Weather Layers</strong>
            </div>
            <div>
                <input type="checkbox" id="wind" checked>
                <label for="wind">Wind</label>
            </div>
            <div>
                <input type="checkbox" id="temp" checked>
                <label for="temp">Temperature</label>
            </div>
            <div>
                <input type="checkbox" id="pressure">
                <label for="pressure">Pressure</label>
            </div>
            <div>
                <input type="checkbox" id="clouds">
                <label for="clouds">Clouds</label>
            </div>
        </div>
        """
        m.get_root().html.add_child(folium.Element(controls_html))

def main():
    # Create map instance
    windy_map = WindyMapReplica()
    
    # Generate map
    m = windy_map.create_map()
    
    # Save to HTML file
    m.save('windy_replica.html')
