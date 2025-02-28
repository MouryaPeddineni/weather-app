# # import numpy as np
# # from moviepy.editor import VideoFileClip, ImageSequenceClip
# # from moviepy.video.fx.all import mask_color
# # import cv2

# # # Step 1: Load the original video
# # video = VideoFileClip("map_video.mp4")

# # # Step 2: Create an animated mask (expanding circle effect)
# # mask_frames = []
# # for t in np.linspace(0, 1, int(video.fps * video.duration)):  # Convert to int
# #     frame = np.zeros((video.h, video.w), dtype=np.uint8)  # Black background
    
# #     # Dynamic expanding circle (mask animation)
# #     radius = int(min(video.h, video.w) * t)  # Expanding radius
# #     cv2.circle(frame, (video.w // 2, video.h // 2), radius, 255, -1)  # White mask
    
# #     mask_frames.append(frame)

# # # print(mask_frames)

# # # Step 3: Convert masks into a MoviePy video clip
# # print(f"Total mask frames generated: {len(mask_frames)}")
# # frame = np.stack([frame]*3, axis=-1)  # Convert (H, W) → (H, W, 3)
# # mask_clip = ImageSequenceClip(mask_frames, fps=video.fps).set_duration(video.duration)

# # # Step 4: Apply mask to the video
# # # masked_video = video.set_mask(mask_clip)

# # # # Step 5: Save the masked video
# # # masked_video.write_videofile("masked_video.mp4", codec="libx264", fps=video.fps)


# # import cv2
# # import numpy as np

# # mask_frames = []
# # for t in np.linspace(0, 1, int(video.fps * video.duration)):  # Generate mask per frame
# #     frame = np.zeros((video.h, video.w), dtype=np.uint8)  # Black background
    
# #     # Expanding circle effect
# #     radius = int(min(video.h, video.w) * t)
# #     cv2.circle(frame, (video.w // 2, video.h // 2), radius, 255, -1)  # White mask
    
# #     frame_rgb = np.stack([frame]*3, axis=-1)  # Convert to (H, W, 3)
# #     mask_frames.append(frame_rgb)

# # print(f"Generated {len(mask_frames)} mask frames.")
# # print(mask_frames[0].shape)  # Should be (height, width, 3)


# # import cv2
# # import numpy as np
# # from moviepy.editor import VideoFileClip, ImageSequenceClip

# # # Step 1: Load the original video
# # video = VideoFileClip("map_video.mp4")

# # # Step 2: Generate animated mask frames (expanding circle effect)
# # mask_frames = []
# # frame_count = int(video.fps * video.duration)  # Total frames

# # for t in np.linspace(0, 1, frame_count):  # Loop over time
# #     frame = np.zeros((video.h, video.w), dtype=np.uint8)  # Black background
    
# #     # Expanding circle effect
# #     radius = int(min(video.h, video.w) * t)  # Expanding radius
# #     cv2.circle(frame, (video.w // 2, video.h // 2), radius, 255, -1)  # White mask
    
# #     # Convert single-channel grayscale mask to 3-channel RGB
# #     frame_rgb = np.stack([frame] * 3, axis=-1)  # Shape: (H, W, 3)
    
# #     mask_frames.append(frame_rgb)

# # # Debugging: Check if frames are generated
# # print(f"Generated {len(mask_frames)} mask frames.")
# # print(f"First frame shape: {mask_frames[0].shape}")  # Should be (H, W, 3)

# # # Step 3: Convert mask frames to a MoviePy clip
# # # Convert mask frames to grayscale and set ismask=True
# # mask_clip = ImageSequenceClip(mask_frames, fps=video.fps).set_duration(video.duration).fx(vfx.colorx, 0).set_mask()

# # # Step 4: Apply the mask to the video
# # masked_video = video.set_mask(mask_clip)

# # # Step 5: Save the final video
# # masked_video.write_videofile("masked_video.mp4", codec="libx264", fps=video.fps)

# # import cv2
# # import numpy as np
# # from moviepy.editor import VideoFileClip, ImageSequenceClip

# # # Step 1: Load the original video
# # video = VideoFileClip("map_video.mp4")

# # # Step 2: Generate animated mask frames (expanding circle effect)
# # mask_frames = []
# # frame_count = int(video.fps * video.duration)  # Total frames

# # for t in np.linspace(0, 1, frame_count):  
# #     frame = np.zeros((video.h, video.w), dtype=np.uint8)  # Grayscale mask (H, W)
    
# #     # Expanding circle effect
# #     radius = int(min(video.h, video.w) * t)  # Expanding radius
# #     cv2.circle(frame, (video.w // 2, video.h // 2), radius, 255, -1)  # White mask

# #     # ✅ Convert grayscale to RGB (H, W, 3) for MoviePy compatibility
# #     frame_rgb = np.stack([frame] * 3, axis=-1)  

# #     mask_frames.append(frame_rgb)

# # # Debugging: Check shape of first frame
# # print(f"Generated {len(mask_frames)} mask frames.")
# # print(f"First frame shape: {mask_frames[0].shape}")  # Should be (H, W, 3)

# # # Step 3: Convert mask frames to a MoviePy mask clip
# # mask_clip = ImageSequenceClip(mask_frames, fps=video.fps).set_duration(video.duration)
# # mask_clip.ismask = True  # ✅ Set it as a mask

# # # Step 4: Apply the mask to the video
# # masked_video = video.set_mask(mask_clip)

# # # Step 5: Save the final video
# # masked_video.write_videofile("masked_video.mp4", codec="libx264", fps=video.fps)

# # import folium
# # from folium import plugins
# # import json


# # def create_animated_map(center_lat, center_lng, markers_data):
# #     """
# #     Create a Folium map with animated markers using alpha channel effects.
    
# #     Parameters:
# #     center_lat (float): Center latitude for the map
# #     center_lng (float): Center longitude for the map
# #     markers_data (list): List of dictionaries containing marker information
# #                         [{'lat': float, 'lng': float, 'name': str}, ...]
    
# #     Returns:
# #     folium.Map: Map object with animated markers
# #     """
# #     # Create base map
# #     m = folium.Map(location=[center_lat, center_lng], zoom_start=10)
    
# #     # Create feature group for markers
# #     marker_cluster = folium.FeatureGroup(name='Animated Markers')
    
# #     # Create the CSS animation for the markers
# #     css = """
# #     @keyframes pulse {
# #         0% { opacity: 0.3; }
# #         50% { opacity: 1; }
# #         100% { opacity: 0.3; }
# #     }
    
# #     .animated-marker {
# #         animation: pulse 2s infinite;
# #     }
# #     """
    
# #     # Add CSS to the map
# #     m.get_root().header.add_child(folium.Element(f'<style>{css}</style>'))
    
# #     # Add markers with custom icons and animation
# #     for marker in markers_data:
# #         # Create custom icon with CSS animation
# #         icon_html = f'''
# #             <div class="animated-marker">
# #                 <i class="fa fa-map-marker fa-3x" style="color: red;"></i>
# #             </div>
# #         '''
        
# #         icon = folium.DivIcon(
# #             html=icon_html,
# #             icon_size=(30, 30),
# #             icon_anchor=(15, 30)
# #         )
        
# #         # Create popup content
# #         popup_content = f"""
# #         <div style="width: 200px;">
# #             <h4>{marker['name']}</h4>
# #             <p>Latitude: {marker['lat']:.4f}</p>
# #             <p>Longitude: {marker['lng']:.4f}</p>
# #         </div>
# #         """
        
# #         # Add marker to the map
# #         folium.Marker(
# #             location=[marker['lat'], marker['lng']],
# #             popup=folium.Popup(popup_content, max_width=300),
# #             icon=icon
# #         ).add_to(marker_cluster)
    
# #     # Add marker cluster to map
# #     marker_cluster.add_to(m)
    
# #     # Add layer control
# #     folium.LayerControl().add_to(m)
    
# #     return m

# # # Example usage
# # if __name__ == "__main__":
# #     # Sample data
# #     sample_markers = [
# #         {"lat": 40.7128, "lng": -74.0060, "name": "New York"},
# #         {"lat": 34.0522, "lng": -118.2437, "name": "Los Angeles"},
# #         {"lat": 41.8781, "lng": -87.6298, "name": "Chicago"}
# #     ]
    
# #     # Create map centered on New York
# #     map_object = create_animated_map(40.7128, -74.0060, sample_markers)
    
# #     # Save map to HTML file
# #     map_object.save('animated_markers_map.html')

# # import folium
# # from folium import plugins
# # import numpy as np

# # def create_wind_map(center_lat, center_lng, wind_data=None):
# #     """
# #     Create a Folium map with wind animation overlay.
    
# #     Parameters:
# #     center_lat (float): Center latitude for the map
# #     center_lng (float): Center longitude for the map
# #     wind_data (dict): Optional dictionary containing wind data
# #                      If None, generates sample wind data
    
# #     Returns:
# #     folium.Map: Map object with wind animation
# #     """
# #     # Create base map
# #     m = folium.Map(location=[center_lat, center_lng], 
# #                   zoom_start=6,
# #                   tiles='cartodbpositron')
    
# #     # If no wind data provided, generate sample data
# #     if wind_data is None:
# #         # Create a grid of wind data
# #         x_dim, y_dim = 50, 50
# #         lat_range = np.linspace(center_lat - 5, center_lat + 5, x_dim)
# #         lon_range = np.linspace(center_lng - 5, center_lng + 5, y_dim)
        
# #         # Generate sample wind vectors (U = east/west, V = north/south)
# #         U = np.ones((y_dim, x_dim)) * 5  # 5 m/s wind from west
# #         V = np.ones((y_dim, x_dim)) * 3  # 3 m/s wind from south
        
# #         # Add some variation to make it more realistic
# #         U = U + np.random.randn(y_dim, x_dim) * 2
# #         V = V + np.random.randn(y_dim, x_dim) * 2
        
# #         wind_data = {
# #             'lat': lat_range,
# #             'lon': lon_range,
# #             'U': U,
# #             'V': V
# #         }
    
# #     # Create wind velocity layer
# #     wind = plugins.VelocityGrid(
# #         data={
# #             'lat': wind_data['lat'].tolist(),
# #             'lon': wind_data['lon'].tolist(),
# #             'U': wind_data['U'].tolist(),
# #             'V': wind_data['V'].tolist()
# #         },
# #         lat_dim='lat',
# #         lon_dim='lon',
# #         velocity_scale=0.01,  # Scale factor for wind velocity
# #         max_velocity=20,      # Maximum wind speed
# #         color_scale=['#2468E8', '#3C9F50', '#E8D725', '#E85225'],  # Blue to red color scale
# #     )
    
# #     # Add wind layer to map
# #     wind.add_to(m)
    
# #     # Add a simple marker if needed
# #     folium.Marker(
# #         [center_lat, center_lng],
# #         popup='Center Point',
# #         icon=folium.Icon(color='red', icon='info-sign')
# #     ).add_to(m)
    
# #     # Add layer control
# #     folium.LayerControl().add_to(m)
    
# #     return m

# # # Example usage with real wind data format
# # def create_real_wind_data(lat_min, lat_max, lon_min, lon_max, resolution=50):
# #     """
# #     Create more realistic wind data for a given region.
# #     This is a sample - in practice, you'd want to use real meteorological data.
# #     """
# #     lat = np.linspace(lat_min, lat_max, resolution)
# #     lon = np.linspace(lon_min, lon_max, resolution)
    
# #     # Create more complex wind patterns
# #     U = np.zeros((resolution, resolution))
# #     V = np.zeros((resolution, resolution))
    
# #     # Create a circular wind pattern
# #     for i in range(resolution):
# #         for j in range(resolution):
# #             x = (i - resolution/2) / (resolution/2)
# #             y = (j - resolution/2) / (resolution/2)
# #             distance = np.sqrt(x**2 + y**2)
# #             angle = np.arctan2(y, x)
            
# #             # Circular wind pattern with some variation
# #             U[i,j] = -5 * y / (distance + 0.1) + np.random.randn() * 0.5
# #             V[i,j] = 5 * x / (distance + 0.1) + np.random.randn() * 0.5
    
# #     return {
# #         'lat': lat,
# #         'lon': lon,
# #         'U': U,
# #         'V': V
# #     }

# # # Example usage
# # if __name__ == "__main__":
# #     # Create map centered on a location
# #     center_lat, center_lng = 40.7128, -74.0060  # New York coordinates
    
# #     # Generate realistic wind data
# #     wind_data = create_real_wind_data(
# #         lat_min=35.7128, 
# #         lat_max=45.7128,
# #         lon_min=-79.0060,
# #         lon_max=-69.0060
# #     )
    
# #     # Create and save map
# #     map_object = create_wind_map(center_lat, center_lng, wind_data)
# #     map_object.save('wind_animation_map.html')

# # import folium
# # from folium import plugins
# # import numpy as np

# # def create_wind_map(center_lat, center_lng, wind_data=None):
# #     """
# #     Create a Folium map with wind animation overlay using the windjs plugin.
    
# #     Parameters:
# #     center_lat (float): Center latitude for the map
# #     center_lng (float): Center longitude for the map
# #     wind_data (dict): Optional dictionary containing wind data
    
# #     Returns:
# #     folium.Map: Map object with wind animation
# #     """
# #     # Create base map
# #     m = folium.Map(location=[center_lat, center_lng], 
# #                   zoom_start=6,
# #                   tiles='cartodbpositron')
    
# #     # Add WindJS plugin
# #     plugins.WindJSPlugin().add_to(m)
    
# #     # Generate sample wind data if none provided
# #     if wind_data is None:
# #         wind_data = {
# #             'speed': np.random.randint(0, 15, size=(20, 20)),  # Wind speed in m/s
# #             'direction': np.random.randint(0, 360, size=(20, 20))  # Wind direction in degrees
# #         }
    
# #     # Add wind data to the map using custom JavaScript
# #     wind_js = f"""
# #         var windData = {{
# #             data: {wind_data},
# #             minVelocity: 0,
# #             maxVelocity: 15,
# #             velocityScale: 0.005,
# #             particleAge: 90,
# #             lineWidth: 1,
# #             particleMultiplier: 0.01,
# #             frameRate: 15,
# #             colorScale: ['rgb(36,104,232)', 'rgb(60,159,80)', 'rgb(232,215,37)', 'rgb(232,82,37)']
# #         }};
        
# #         var velocityLayer = L.velocityLayer(windData);
# #         velocityLayer.addTo(map);
# #     """
    
# #     # Add the JavaScript to the map
# #     m.get_root().script.add_child(folium.Element(wind_js))
    
# #     return m

# # # Example usage
# # if __name__ == "__main__":
# #     # First, install required packages:
# #     # pip install folium
# #     # pip install numpy
    
# #     # You'll also need to include the Leaflet Velocity library in your HTML
# #     center_lat, center_lng = 40.7128, -74.0060  # New York coordinates
# #     map_object = create_wind_map(center_lat, center_lng)
# #     map_object.save('wind_animation_map.html')

# import folium
# from folium import plugins
# import numpy as np

# def create_wind_direction_map(center_lat, center_lng, num_markers=20):
#     """
#     Create a Folium map with wind direction indicators using BoatMarker plugin.
    
#     Parameters:
#     center_lat (float): Center latitude for the map
#     center_lng (float): Center longitude for the map
#     num_markers (int): Number of markers to create in each direction
    
#     Returns:
#     folium.Map: Map object with wind direction indicators
#     """
#     # Create base map
#     m = folium.Map(location=[center_lat, center_lng], 
#                   zoom_start=6,
#                   tiles='cartodbpositron')
    
#     # Create a grid of points
#     lat_range = np.linspace(center_lat - 2, center_lat + 2, num_markers)
#     lon_range = np.linspace(center_lng - 2, center_lng + 2, num_markers)
    
#     # Add boat markers with different wind directions
#     for lat in lat_range:
#         for lon in lon_range:
#             # Generate random wind direction (0-360 degrees)
#             # In real application, this would come from your wind data
#             wind_direction = np.random.randint(0, 360)
            
#             # Create boat marker
#             plugins.BoatMarker(
#                 (lat, lon),
#                 heading=wind_direction,
#                 wind_heading=wind_direction,
#                 wind_speed=10,  # Set wind speed (knots)
#                 color='#8b0000'  # Dark red color
#             ).add_to(m)
    
#     # Add a legend
#     legend_html = '''
#         <div style="position: fixed; 
#                     bottom: 50px; right: 50px; width: 150px; height: 90px; 
#                     border:2px solid grey; z-index:9999; font-size:14px;
#                     background-color:white;
#                     padding: 10px;
#                     border-radius: 5px;">
#             <p><b>Wind Direction Legend</b></p>
#             <p>🔺 indicates direction<br>
#                Length shows speed</p>
#         </div>
#         '''
#     m.get_root().html.add_child(folium.Element(legend_html))
    
#     return m

# def create_animated_wind_markers(m, center_lat, center_lng, num_markers=5):
#     """
#     Add animated circle markers to show wind intensity areas
#     """
#     for _ in range(num_markers):
#         # Create random positions near the center
#         lat = center_lat + np.random.uniform(-1, 1)
#         lng = center_lng + np.random.uniform(-1, 1)
        
#         # Add a circle marker with radius animation
#         folium.CircleMarker(
#             location=[lat, lng],
#             radius=20,
#             color='blue',
#             fill=True,
#             fillColor='blue',
#             fillOpacity=0.2,
#             popup=f'Wind Speed: {np.random.randint(5, 15)} m/s'
#         ).add_to(m)

# # Example usage
# if __name__ == "__main__":
#     # Create map centered on a location (e.g., New York)
#     center_lat, center_lng = 40.7128, -74.0060
    
#     # Create base map with wind direction markers
#     map_object = create_wind_direction_map(center_lat, center_lng)
    
#     # Add animated markers for wind intensity
#     create_animated_wind_markers(map_object, center_lat, center_lng)
    
#     # Save the map
#     map_object.save('wind_direction_map.html')

# import folium
# import numpy as np
# from folium import plugins

# def create_weather_mask_map(center_lat, center_lng, weather_data=None):
#     """
#     Create a Folium map with weather condition masks.
    
#     Parameters:
#     center_lat (float): Center latitude for the map
#     center_lng (float): Center longitude for the map
#     weather_data (dict): Dictionary containing weather conditions and their areas
#     """
#     # Create base map
#     m = folium.Map(location=[center_lat, center_lng], 
#                   zoom_start=8,
#                   tiles='cartodbpositron')
    
#     # Add custom CSS for weather masks
#     custom_css = """
#         <style>
#             .rain-mask {
#                 background: repeating-linear-gradient(
#                     -45deg,
#                     rgba(0, 0, 255, 0.2),
#                     rgba(0, 0, 255, 0.2) 1px,
#                     rgba(0, 0, 255, 0.3) 1px,
#                     rgba(0, 0, 255, 0.3) 3px
#                 );
#             }
#             .snow-mask {
#                 background: radial-gradient(
#                     circle at center,
#                     rgba(255, 255, 255, 0.4) 0%,
#                     rgba(255, 255, 255, 0.1) 100%
#                 );
#             }
#             .cloudy-mask {
#                 background: rgba(128, 128, 128, 0.3);
#             }
#             .sunny-mask {
#                 background: rgba(255, 255, 0, 0.1);
#             }
#             .fog-mask {
#                 background: rgba(120, 120, 120, 0.1);
#             }
#         </style>
#     """
#     m.get_root().header.add_child(folium.Element(custom_css))
    
#     # If no weather data provided, create sample data
#     if weather_data is None:
#         weather_data = generate_sample_weather_areas(center_lat, center_lng)
    
#     # Add weather condition masks
#     for condition in weather_data:
#         coords = condition['coordinates']
#         weather_type = condition['type']
#         intensity = condition.get('intensity', 1.0)
        
#         # Create style based on weather type
#         style_dict = get_weather_style(weather_type, intensity)
        
#         # Add polygon with weather mask
#         folium.GeoJson(
#             {
#                 'type': 'Feature',
#                 'geometry': {
#                     'type': 'Polygon',
#                     'coordinates': [coords]
#                 }
#             },
#             style_function=lambda x: style_dict,
#             tooltip=f"{weather_type.title()} Area"
#         ).add_to(m)
    
#     # Add legend
#     add_weather_legend(m)
    
#     return m

# def generate_sample_weather_areas(center_lat, center_lng):
#     """Generate sample weather areas around the center point."""
#     weather_types = ['rain', 'snow', 'cloudy', 'sunny', 'fog']
#     weather_areas = []
    
#     for i, w_type in enumerate(weather_types):
#         # Create a polygon area for each weather type
#         angle = i * (360 / len(weather_types))
#         radius = 0.5  # degrees
        
#         coords = []
#         for j in range(8):  # Create an octagon
#             a = angle + (j * 45)
#             lat = center_lat + radius * np.cos(np.radians(a))
#             lng = center_lng + radius * np.sin(np.radians(a))
#             coords.append([lng, lat])
        
#         # Close the polygon
#         coords.append(coords[0])
        
#         weather_areas.append({
#             'type': w_type,
#             'coordinates': coords,
#             'intensity': np.random.uniform(0.5, 1.0)
#         })
    
#     return weather_areas

# def get_weather_style(weather_type, intensity=1.0):
#     """Return style dictionary for weather type."""
#     base_style = {
#         'fillOpacity': 0.7 * intensity,
#         'weight': 1,
#         'color': 'white',
#         'className': f'{weather_type}-mask'
#     }
#     return base_style

# def add_weather_legend(m):
#     """Add a legend showing weather condition types."""
#     legend_html = """
#         <div style="position: fixed; 
#                     bottom: 50px; right: 50px; 
#                     width: 150px;
#                     background-color: white;
#                     padding: 10px;
#                     border-radius: 5px;
#                     border: 2px solid grey;
#                     z-index: 9999;">
#             <p style="margin-bottom: 5px;"><strong>Weather Conditions</strong></p>
#             <div style="margin-bottom: 5px;">
#                 <div class="rain-mask" style="display: inline-block; width: 20px; height: 20px;"></div>
#                 <span style="margin-left: 5px;">Rain</span>
#             </div>
#             <div style="margin-bottom: 5px;">
#                 <div class="snow-mask" style="display: inline-block; width: 20px; height: 20px;"></div>
#                 <span style="margin-left: 5px;">Snow</span>
#             </div>
#             <div style="margin-bottom: 5px;">
#                 <div class="cloudy-mask" style="display: inline-block; width: 20px; height: 20px;"></div>
#                 <span style="margin-left: 5px;">Cloudy</span>
#             </div>
#             <div style="margin-bottom: 5px;">
#                 <div class="sunny-mask" style="display: inline-block; width: 20px; height: 20px;"></div>
#                 <span style="margin-left: 5px;">Sunny</span>
#             </div>
#             <div>
#                 <div class="fog-mask" style="display: inline-block; width: 20px; height: 20px;"></div>
#                 <span style="margin-left: 5px;">Fog</span>
#             </div>
#         </div>
#     """
#     m.get_root().html.add_child(folium.Element(legend_html))

# # Example usage
# if __name__ == "__main__":
#     # Create map centered on a location (e.g., New York)
#     center_lat, center_lng = 30.9164, 66.4986
    
#     # Create and save map
#     map_object = create_weather_mask_map(center_lat, center_lng)
#     map_object.save('weather_masks_map.html')

# import folium
# import numpy as np
# from folium import plugins

# def create_weather_mask_map(center_lat, center_lng, weather_data=None):
#     """
#     Create a Folium map with semi-transparent weather condition masks.
    
#     Parameters:
#     center_lat (float): Center latitude for the map
#     center_lng (float): Center longitude for the map
#     weather_data (dict): Dictionary containing weather conditions and their areas
#     """
#     # Create base map
#     m = folium.Map(location=[center_lat, center_lng], 
#                   zoom_start=8,
#                   tiles='cartodbpositron')
    
#     # Add custom CSS with reduced opacity for weather masks
#     custom_css = """
#         <style>
#             .rain-mask {
#                 background: repeating-linear-gradient(
#                     -45deg,
#                     rgba(0, 0, 255, 0.1),
#                     rgba(0, 0, 255, 0.1) 1px,
#                     rgba(0, 0, 255, 0.15) 1px,
#                     rgba(0, 0, 255, 0.15) 3px
#                 );
#             }
#             .snow-mask {
#                 background: radial-gradient(
#                     circle at center,
#                     rgba(255, 255, 255, 0.2) 0%,
#                     rgba(255, 255, 255, 0.05) 100%
#                 );
#             }
#             .cloudy-mask {
#                 background: rgba(128, 128, 128, 0.15);
#             }
#             .sunny-mask {
#                 background: rgba(255, 255, 0, 0.05);
#             }
#             .fog-mask {
#                 background: rgba(200, 200, 200, 0.2);
#             }
#         </style>
#     """
#     m.get_root().header.add_child(folium.Element(custom_css))
    
#     # If no weather data provided, create sample data
#     if weather_data is None:
#         weather_data = generate_sample_weather_areas(center_lat, center_lng)
    
#     # Add weather condition masks with reduced opacity
#     for condition in weather_data:
#         coords = condition['coordinates']
#         weather_type = condition['type']
#         intensity = condition.get('intensity', 0.5)  # Reduced default intensity
        
#         # Create style based on weather type
#         style_dict = get_weather_style(weather_type, intensity)
        
#         # Add polygon with weather mask
#         folium.GeoJson(
#             {
#                 'type': 'Feature',
#                 'geometry': {
#                     'type': 'Polygon',
#                     'coordinates': [coords]
#                 }
#             },
#             style_function=lambda x: style_dict,
#             tooltip=f"{weather_type.title()} Area"
#         ).add_to(m)
    
#     # Add legend with matching reduced opacity examples
#     add_weather_legend(m)
    
#     return m

# def generate_sample_weather_areas(center_lat, center_lng):
#     """Generate sample weather areas around the center point."""
#     weather_types = ['rain', 'snow', 'cloudy', 'sunny', 'fog']
#     weather_areas = []
    
#     for i, w_type in enumerate(weather_types):
#         angle = i * (360 / len(weather_types))
#         radius = 0.5  # degrees
        
#         coords = []
#         for j in range(8):  # Create an octagon
#             a = angle + (j * 45)
#             lat = center_lat + radius * np.cos(np.radians(a))
#             lng = center_lng + radius * np.sin(np.radians(a))
#             coords.append([lng, lat])
        
#         # Close the polygon
#         coords.append(coords[0])
        
#         weather_areas.append({
#             'type': w_type,
#             'coordinates': coords,
#             'intensity': np.random.uniform(0.3, 0.6)  # Reduced intensity range
#         })
    
#     return weather_areas

# def get_weather_style(weather_type, intensity=0.5):
#     """Return style dictionary for weather type with reduced opacity."""
#     base_style = {
#         'fillOpacity': 0.4 * intensity,  # Reduced fill opacity
#         'weight': 1,
#         'opacity': 0.3,  # Reduced border opacity
#         'color': 'white',
#         'className': f'{weather_type}-mask'
#     }
#     return base_style

# def add_weather_legend(m):
#     """Add a legend showing weather condition types with matching reduced opacity."""
#     legend_html = """
#         <div style="position: fixed; 
#                     bottom: 50px; right: 50px; 
#                     width: 150px;
#                     background-color: rgba(255, 255, 255, 0.9);
#                     padding: 10px;
#                     border-radius: 5px;
#                     border: 1px solid rgba(128, 128, 128, 0.5);
#                     z-index: 9999;">
#             <p style="margin-bottom: 5px;"><strong>Weather Conditions</strong></p>
#             <div style="margin-bottom: 5px;">
#                 <div class="rain-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
#                 <span style="margin-left: 5px;">Rain</span>
#             </div>
#             <div style="margin-bottom: 5px;">
#                 <div class="snow-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
#                 <span style="margin-left: 5px;">Snow</span>
#             </div>
#             <div style="margin-bottom: 5px;">
#                 <div class="cloudy-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
#                 <span style="margin-left: 5px;">Cloudy</span>
#             </div>
#             <div style="margin-bottom: 5px;">
#                 <div class="sunny-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
#                 <span style="margin-left: 5px;">Sunny</span>
#             </div>
#             <div>
#                 <div class="fog-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
#                 <span style="margin-left: 5px;">Fog</span>
#             </div>
#         </div>
#     """
#     m.get_root().html.add_child(folium.Element(legend_html))

# # Example usage
# if __name__ == "__main__":
#     # Create map centered on a location (e.g., New York)
#     center_lat, center_lng = 40.7128, -74.0060
    
#     # Create and save map
#     map_object = create_weather_mask_map(center_lat, center_lng)
#     map_object.save('weather_masks_map.html')


import folium
import numpy as np
from folium import plugins


# def create_animated_weather_map(center_lat, center_lng, weather_data=None):
#     """
#     Create a Folium map with animated weather condition masks.
#     """
#     # Create base map
#     m = folium.Map(location=[center_lat, center_lng], 
#                   zoom_start=8,
#                   tiles='cartodbpositron')
    
#     # Add custom CSS for animated weather effects
#     custom_css = """
#         <style>
#             /* Previous animations remain the same */
#             @keyframes snowfall {
#                 0% {
#                     background-position: 0px 0px, 0px 0px, 0px 0px;
#                 }
#                 100% {
#                     background-position: 500px 1000px, 400px 400px, 300px 300px;
#                 }
#             }
            
#             .snow-mask {
#                 background-image: 
#                     radial-gradient(4px 4px at 100px 50px, white 50%, transparent 50%),
#                     radial-gradient(6px 6px at 200px 150px, white 50%, transparent 50%),
#                     radial-gradient(3px 3px at 300px 250px, white 50%, transparent 50%);
#                 background-size: 600px 600px;
#                 animation: snowfall 20s linear infinite;
#                 opacity: 0.15;
#             }
            
#             /* Enhanced fog animation with curved lines */
#             @keyframes fogFlow1 {
#                 0% { transform: translateX(-100%) translateY(0%); }
#                 100% { transform: translateX(100%) translateY(-20%); }
#             }
            
#             @keyframes fogFlow2 {
#                 0% { transform: translateX(-100%) translateY(-10%); }
#                 100% { transform: translateX(100%) translateY(10%); }
#             }
            
#             @keyframes fogFlow3 {
#                 0% { transform: translateX(-100%) translateY(10%); }
#                 100% { transform: translateX(100%) translateY(-10%); }
#             }
            
#             .fog-mask {
#                 position: relative;
#                 overflow: hidden;
#             }
            
#             .fog-mask::before,
#             .fog-mask::after,
#             .fog-mask::after {
#                 content: '';
#                 position: absolute;
#                 top: 0;
#                 left: 0;
#                 right: 0;
#                 bottom: 0;
#                 background-image: 
#                     url("data:image/svg+xml,%3Csvg width='400' height='100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0,50 Q100,30 200,50 T400,50' stroke='white' fill='none' stroke-width='50' stroke-opacity='0.15'/%3E%3C/svg%3E");
#                 background-size: 400px 100px;
#                 opacity: 0.3;
#             }
            
#             .fog-mask::before {
#                 animation: fogFlow1 15s linear infinite;
#             }
            
#             .fog-mask::after {
#                 animation: fogFlow2 18s linear infinite;
#                 background-position-y: 33%;
#             }
            
#             .fog-mask::after {
#                 animation: fogFlow3 20s linear infinite;
#                 background-position-y: 66%;
#             }
            
#             /* Other weather effects remain the same */
#             .rain-mask {
#                 background: repeating-linear-gradient(
#                     to bottom,
#                     transparent 0px,
#                     transparent 5px,
#                     rgba(0, 0, 255, 0.1) 5px,
#                     rgba(0, 0, 255, 0.1) 10px
#                 );
#                 background-size: 100% 20px;
#                 animation: rainfall 1s linear infinite;
#                 opacity: 0.2;
#             }
            
#             @keyframes rainfall {
#                 0% { background-position: 0px 0px; }
#                 100% { background-position: 0px 1000px; }
#             }
            
#             .cloudy-mask {
#                 background: repeating-radial-gradient(
#                     circle at 50% 50%,
#                     rgba(128, 128, 128, 0.1) 0%,
#                     rgba(128, 128, 128, 0.2) 40%,
#                     rgba(128, 128, 128, 0.1) 50%
#                 );
#                 background-size: 200px 200px;
#                 animation: cloudsMove 30s linear infinite;
#                 opacity: 0.15;
#             }
            
#             @keyframes cloudsMove {
#                 0% { background-position: 0px 0px; }
#                 100% { background-position: 1000px 0px; }
#             }
            
#             .sunny-mask {
#                 background: radial-gradient(
#                     circle at 50% 50%,
#                     rgba(255, 255, 0, 0.05) 0%,
#                     transparent 70%
#                 );
#             }
#         </style>
#     """
#     m.get_root().header.add_child(folium.Element(custom_css))
    
#     # Rest of the code remains the same
#     if weather_data is None:
#         weather_data = generate_sample_weather_areas(center_lat, center_lng)
    
#     for condition in weather_data:
#         coords = condition['coordinates']
#         weather_type = condition['type']
#         intensity = condition.get('intensity', 0.5)
        
#         style_dict = get_weather_style(weather_type, intensity)
        
#         folium.GeoJson(
#             {
#                 'type': 'Feature',
#                 'geometry': {
#                     'type': 'Polygon',
#                     'coordinates': [coords]
#                 }
#             },
#             style_function=lambda x, style=style_dict: style,
#             tooltip=f"{weather_type.title()} Area"
#         ).add_to(m)
    
#     add_weather_legend(m)
#     return m


import folium
import numpy as np


def get_weather_style(weather_type, intensity=0.5):
    return {
        'fillOpacity': 1.0,
        'weight': 1,
        'opacity': 0.3,
        'color': 'white',
        'className': f'{weather_type}-mask'
    }



def generate_sample_weather_areas(center_lat, center_lng):
    """Generate sample weather areas around the center point."""
    weather_types = ['rain', 'snow', 'cloudy', 'sunny', 'fog']
    weather_areas = []
    
    for i, w_type in enumerate(weather_types):
        angle = i * (360 / len(weather_types))
        radius = 0.5
        
        coords = []
        for j in range(8):
            a = angle + (j * 45)
            lat = center_lat + radius * np.cos(np.radians(a))
            lng = center_lng + radius * np.sin(np.radians(a))
            coords.append([lng, lat])
        
        coords.append(coords[0])
        
        weather_areas.append({
            'type': w_type,
            'coordinates': coords,
            'intensity': np.random.uniform(0.3, 0.6)
        })
    
    return weather_areas

def add_weather_legend(m):
    """Add a legend showing weather condition types."""
    legend_html = """
        <div style="position: fixed; 
                    bottom: 50px; right: 50px; 
                    width: 150px;
                    background-color: rgba(255, 255, 255, 0.9);
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid rgba(128, 128, 128, 0.5);
                    z-index: 9999;">
            <p style="margin-bottom: 5px;"><strong>Weather Conditions</strong></p>
            <div style="margin-bottom: 5px;">
                <div class="rain-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
                <span style="margin-left: 5px;">Rain</span>
            </div>
            <div style="margin-bottom: 5px;">
                <div class="snow-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
                <span style="margin-left: 5px;">Snow</span>
            </div>
            <div style="margin-bottom: 5px;">
                <div class="cloudy-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
                <span style="margin-left: 5px;">Cloudy</span>
            </div>
            <div style="margin-bottom: 5px;">
                <div class="sunny-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
                <span style="margin-left: 5px;">Sunny</span>
            </div>
            <div>
                <div class="fog-mask" style="display: inline-block; width: 20px; height: 20px; border: 1px solid rgba(0,0,0,0.1);"></div>
                <span style="margin-left: 5px;">Fog</span>
            </div>
        </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))


def create_full_weather_map(center_lat, center_lng):
    """
    Create a Folium map with animated weather conditions covering the entire map.
    """
    # Create base map
    m = folium.Map(location=[center_lat, center_lng], 
                  zoom_start=5,
                  tiles='cartodbpositron')
    
    custom_css = """
        <style>
            /* Enhanced Rain Animation */
@keyframes raindrop-fall {
    0% {
        transform: translateY(-10px) translateX(-5px) skewX(-10deg);
        opacity: 0;
    }
    10% {
        opacity: 0.7;
    }
    90% {
        opacity: 0.7;
    }
    100% {
        transform: translateY(100px) translateX(5px) skewX(-10deg);
        opacity: 0;
    }
}

.rain-mask {
    background-color: rgba(0, 0, 255, 0.05);
    position: relative;
    overflow: hidden;
}

.rain-mask::before,
.rain-mask::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background-image: 
        repeating-linear-gradient(
            170deg,
            transparent 0px,
            transparent 4px,
            rgba(79, 149, 255, 0.5) 4px,
            rgba(79, 149, 255, 0.5) 6px
        ),
        repeating-linear-gradient(
            170deg,
            transparent 0px,
            transparent 3px,
            rgba(79, 149, 255, 0.3) 3px,
            rgba(79, 149, 255, 0.3) 5px
        );
    background-size: 100% 20px;
}

.rain-mask::before {
    animation: rainfall 0.8s linear infinite;
    opacity: 0.4;
}

.rain-mask::after {
    animation: rainfall 1.2s linear infinite;
    opacity: 0.3;
    background-position: -10px -20px;
}

@keyframes rainfall {
    0% {
        transform: translateY(-20px) translateX(-2px);
    }
    100% {
        transform: translateY(20px) translateX(2px);
    }
}

/* Heavy Rain Variation */
.heavy-rain-mask {
    background-color: rgba(0, 0, 255, 0.08);
}

.heavy-rain-mask::before,
.heavy-rain-mask::after {
    background-image: 
        repeating-linear-gradient(
            170deg,
            transparent 0px,
            transparent 3px,
            rgba(79, 149, 255, 0.6) 3px,
            rgba(79, 149, 255, 0.6) 7px
        ),
        repeating-linear-gradient(
            170deg,
            transparent 0px,
            transparent 2px,
            rgba(79, 149, 255, 0.4) 2px,
            rgba(79, 149, 255, 0.4) 6px
        );
    background-size: 100% 15px;
}

.heavy-rain-mask::before {
    animation: rainfall 0.6s linear infinite;
    opacity: 0.5;
}

.heavy-rain-mask::after {
    animation: rainfall 0.8s linear infinite;
    opacity: 0.4;
    background-position: -15px -25px;
}

/* Thunderstorm Animation */
.thunderstorm-mask {
    composes: heavy-rain-mask;
    position: relative;
}

@keyframes lightning {
    0%, 95%, 98% {
        background-color: rgba(0, 0, 255, 0.08);
    }
    96%, 99% {
        background-color: rgba(255, 255, 255, 0.4);
    }
    97%, 100% {
        background-color: rgba(0, 0, 255, 0.08);
    }
}

.thunderstorm-mask {
    animation: lightning 5s infinite;
}

/* Cloud Movement Animation */
@keyframes cloudDrift {
    0% {
        transform: translateX(-10px) scale(1);
        opacity: 0.8;
    }
    50% {
        transform: translateX(10px) scale(1.05);
        opacity: 1;
    }
    100% {
        transform: translateX(-10px) scale(1);
        opacity: 0.8;
    }
}

.cloudy-mask::before {
    animation: cloudDrift 8s ease-in-out infinite;
    background: 
        radial-gradient(
            circle at 50% 50%,
            rgba(255, 255, 255, 0.4) 20%,
            rgba(255, 255, 255, 0.2) 40%,
            rgba(255, 255, 255, 0.1) 60%,
            transparent 70%
        );
}
        </style>
    """
    
    m.get_root().header.add_child(folium.Element(custom_css))
    
    # Keep the rest of your code the same...
    
    weather_regions = [
            {
                'type': 'snow',
                'coordinates': [
                    [center_lng - 5, center_lat + 3],
                    [center_lng - 2, center_lat + 3],
                    [center_lng - 2, center_lat + 5],
                    [center_lng - 5, center_lat + 5],
                ]
            },
            {
                'type': 'rain',
                'coordinates': [
                    [center_lng - 2, center_lat + 1],
                    [center_lng + 1, center_lat + 1],
                    [center_lng + 1, center_lat + 3],
                    [center_lng - 2, center_lat + 3],
                ]
            },
            {
                'type': 'heavy-rain',
                'coordinates': [
                    [center_lng + 1, center_lat + 3],
                    [center_lng + 4, center_lat + 3],
                    [center_lng + 4, center_lat + 5],
                    [center_lng + 1, center_lat + 5],
                ]
            },
            {
                'type': 'fog',
                'coordinates': [
                    [center_lng - 5, center_lat - 1],
                    [center_lng - 2, center_lat - 1],
                    [center_lng - 2, center_lat + 1],
                    [center_lng - 5, center_lat + 1],
                ]
            },
            {
                'type': 'partly-cloudy',
                'coordinates': [
                    [center_lng - 2, center_lat - 1],
                    [center_lng + 1, center_lat - 1],
                    [center_lng + 1, center_lat + 1],
                    [center_lng - 2, center_lat + 1],
                ]
            },
            {
                'type': 'sunny',
                'coordinates': [
                    [center_lng + 1, center_lat - 1],
                    [center_lng + 4, center_lat - 1],
                    [center_lng + 4, center_lat + 1],
                    [center_lng + 1, center_lat + 1],
                ]
            },
            {
                'type': 'thunderstorm',
                'coordinates': [
                    [center_lng - 5, center_lat - 5],
                    [center_lng - 2, center_lat - 5],
                    [center_lng - 2, center_lat - 3],
                    [center_lng - 5, center_lat - 3],
                ]
            }
        ]
    
    # Add weather regions to map
    for region in weather_regions:
        folium.GeoJson(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [region['coordinates']]
                }
            },
            style_function=lambda x, type=region['type']: {
                'fillOpacity': 1.0,
                'weight': 1,
                'opacity': 0.3,
                'color': 'white',
                'className': f"{type}-mask"
            },
            tooltip=f"{region['type'].replace('-', ' ').title()} Area"
        ).add_to(m)
    
    return m

# Example usage
if __name__ == "__main__":
    # Create map centered on New York
    center_lat, center_lng = 40.7128, -74.0060
    map_object = create_full_weather_map(center_lat, center_lng)
    map_object.save('full_weather_map.html')
