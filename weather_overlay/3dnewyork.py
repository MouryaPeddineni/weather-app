# import numpy as np
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# def create_nyc_3d_map(is_sunny=True):
#     # NYC boundaries (approximate)
#     lat_range = np.linspace(40.4, 40.9, 50)
#     lon_range = np.linspace(-74.3, -73.7, 50)
    
#     # Create mesh grid for the surface
#     lon_grid, lat_grid = np.meshgrid(lon_range, lat_range)
    
#     # Create basic elevation data (simplified for demonstration)
#     # In a real application, you'd want to use actual elevation data
#     z_data = np.zeros(lon_grid.shape)
    
#     # Add some random elevation variations to make it more interesting
#     np.random.seed(42)
#     z_data += np.random.rand(*z_data.shape) * 0.1
    
#     # Create the base map
#     fig = go.Figure()
    
#     # Add the surface plot for NYC
#     fig.add_trace(go.Surface(
#         x=lon_grid,
#         y=lat_grid,
#         z=z_data,
#         colorscale='Viridis',
#         showscale=False,
#         lighting=dict(
#             ambient=0.6,
#             diffuse=0.5,
#             fresnel=0.2,
#             specular=0.2,
#             roughness=0.9
#         )
#     ))
    
#     if is_sunny:
#         # Add sun as a scatter3d point
#         fig.add_trace(go.Scatter3d(
#             x=[-73.9],
#             y=[40.9],
#             z=[0.5],
#             mode='markers',
#             marker=dict(
#                 size=50,
#                 color='yellow',
#                 symbol='circle',
#                 line=dict(
#                     color='orange',
#                     width=2
#                 )
#             ),
#             showlegend=False
#         ))
        
#         # Add sun rays as multiple lines
#         ray_count = 20
#         for i in range(ray_count):
#             angle = (2 * np.pi * i) / ray_count
#             end_x = -73.9 + 0.2 * np.cos(angle)
#             end_y = 40.9 + 0.2 * np.sin(angle)
            
#             fig.add_trace(go.Scatter3d(
#                 x=[-73.9, end_x],
#                 y=[40.9, end_y],
#                 z=[0.5, 0.5],
#                 mode='lines',
#                 line=dict(
#                     color='yellow',
#                     width=3
#                 ),
#                 showlegend=False
#             ))
    
#     # Update layout for better 3D visualization
#     fig.update_layout(
#         title='3D New York City Map with Weather Effects',
#         scene=dict(
#             camera=dict(
#                 eye=dict(x=1.5, y=1.5, z=1.5)
#             ),
#             aspectratio=dict(x=1, y=1, z=0.3),
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Elevation'
#         ),
#         showlegend=False,
#         margin=dict(l=0, r=0, t=30, b=0)
#     )
    
#     return fig

# # Create and display the map
# map_fig = create_nyc_3d_map(is_sunny=True)
# map_fig.show()

import numpy as np
import plotly.graph_objects as go
import folium
from folium.plugins import FloatImage
import base64
from io import BytesIO

def create_sun_plotly():
    """Creates a 3D sun with rays using Plotly"""
    fig = go.Figure()

    # Sun position (above NYC)
    sun_x, sun_y, sun_z = -74.006, 40.7128, 0.5

    # Add the sun (large yellow sphere)
    fig.add_trace(go.Scatter3d(
        x=[sun_x], y=[sun_y], z=[sun_z],
        mode='markers',
        marker=dict(
            size=50,
            color='yellow',
            opacity=1,
            symbol='circle'
        ),
        showlegend=False
    ))

    # Add sun rays (20 rays in different directions)
    ray_count = 20
    for i in range(ray_count):
        angle = (2 * np.pi * i) / ray_count
        end_x = sun_x + 0.2 * np.cos(angle)
        end_y = sun_y + 0.2 * np.sin(angle)

        fig.add_trace(go.Scatter3d(
            x=[sun_x, end_x],
            y=[sun_y, end_y],
            z=[sun_z, sun_z],
            mode='lines',
            line=dict(
                color='yellow',
                width=3
            ),
            showlegend=False
        ))

    # Layout settings
    fig.update_layout(
        title="3D Sun over New York",
        scene=dict(
            xaxis_title="Longitude",
            yaxis_title="Latitude",
            zaxis_title="Height",
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)),
        ),
        margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig

def plot_sun_on_folium():
    """Embeds the Plotly 3D Sun into a Folium map"""
    # Generate the 3D sun plot
    fig = create_sun_plotly()

    # Save the Plotly figure as an image
    img_bytes = BytesIO()
    fig.write_image(img_bytes, format="png")
    img_bytes.seek(0)

    # Encode image to base64
    img_base64 = base64.b64encode(img_bytes.read()).decode()

    # Create a Folium map centered on NYC
    m = folium.Map(location=[40.7128, -74.006], zoom_start=10)

    # Add the 3D Sun image overlay
    FloatImage(f"data:image/png;base64,{img_base64}", bottom=10, left=10).add_to(m)

    return m

# Display the folium map with the 3D sun
m = plot_sun_on_folium()
m.save("sun_nyc_map.html")  # Save to an HTML file
m
