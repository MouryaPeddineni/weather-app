import folium
import numpy as np
from folium import plugins


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
            /* Rain Animation */
            @keyframes raindrop-fall {
                0% {
                    transform: translateY(-10px);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(100px);
                    opacity: 0;
                }
            }

            .rain-mask {
                background-color: rgba(0, 0, 255, 0.1);
                position: relative;
                overflow: hidden;
            }

            .rain-mask::before {
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background-image: 
                    repeating-linear-gradient(
                        transparent 0px,
                        transparent 5px,
                        #4F95FF 5px,
                        #4F95FF 10px
                    );
                background-size: 100% 20px;
                animation: rainfall 1s linear infinite;
                opacity: 0.4;
            }

            @keyframes rainfall {
                0% {
                    transform: translateY(-20px);
                }
                100% {
                    transform: translateY(20px);
                }
            }

            /* Cloudy Animation */
            @keyframes cloudMove {
                0% {
                    transform: translateX(-10px);
                }
                50% {
                    transform: translateX(10px);
                }
                100% {
                    transform: translateX(-10px);
                }
            }

            .cloudy-mask {
                background-color: rgba(200, 200, 200, 0.3);
                position: relative;
                overflow: hidden;
            }

            .cloudy-mask::before {
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background-image: 
                    radial-gradient(circle at 50% 50%, 
                        rgba(255, 255, 255, 0.4) 0%,
                        rgba(255, 255, 255, 0.1) 60%,
                        transparent 70%);
                background-size: 100px 100px;
                animation: cloudMove 4s ease-in-out infinite;
            }

            /* Snow Animation */
            @keyframes snowfall {
                0% {
                    transform: translateY(-10px) translateX(-10px);
                }
                100% {
                    transform: translateY(110px) translateX(10px);
                }
            }

            .snow-mask {
                background-color: rgba(255, 255, 255, 0.1);
                position: relative;
                overflow: hidden;
            }

            .snow-mask::before {
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background-image: 
                    radial-gradient(circle at 50% 50%, white 0%, transparent 60%);
                background-size: 15px 15px;
                background-position: 0 0;
                animation: snowfall 3s linear infinite;
            }

            /* Sunny Animation */
            @keyframes sunShine {
                0% {
                    transform: scale(1) rotate(0deg);
                    opacity: 0.7;
                }
                50% {
                    transform: scale(1.1) rotate(180deg);
                    opacity: 0.9;
                }
                100% {
                    transform: scale(1) rotate(360deg);
                    opacity: 0.7;
                }
            }

            .sunny-mask {
                background-color: rgba(255, 255, 0, 0.1);
                position: relative;
                overflow: hidden;
            }

            .sunny-mask::before {
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle at 50% 50%,
                    rgba(255, 255, 0, 0.5) 0%,
                    rgba(255, 255, 0, 0.2) 50%,
                    transparent 70%);
                animation: sunShine 4s ease-in-out infinite;
            }

            /* Fog Animation */
            @keyframes fogMove {
                0% {
                    transform: translateX(-20px);
                    opacity: 0.3;
                }
                50% {
                    transform: translateX(20px);
                    opacity: 0.5;
                }
                100% {
                    transform: translateX(-20px);
                    opacity: 0.3;
                }
            }

            .fog-mask {
                background-color: rgba(200, 200, 200, 0.2);
                position: relative;
                overflow: hidden;
            }

            .fog-mask::before {
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background: linear-gradient(45deg,
                    rgba(255, 255, 255, 0.5) 0%,
                    rgba(255, 255, 255, 0.2) 100%);
                animation: fogMove 5s ease-in-out infinite;
            }

            /* Partly Cloudy Animation - Combination of sunny and cloudy */
            .partly-cloudy-mask {
                background-color: rgba(200, 200, 200, 0.2);
                position: relative;
                overflow: hidden;
            }

            .partly-cloudy-mask::before {
                content: '';
                position: absolute;
                width: 100%;
                height: 100%;
                background: 
                    radial-gradient(circle at 30% 50%,
                        rgba(255, 255, 0, 0.3) 10%,
                        transparent 60%),
                    radial-gradient(circle at 70% 50%,
                        rgba(255, 255, 255, 0.4) 10%,
                        transparent 60%);
                animation: cloudMove 4s ease-in-out infinite;
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
            style_function=lambda x: {
                'fillOpacity': 0,  # Make the polygon transparent
                'weight': 0,
                'opacity': 0
            },
            tooltip=f"{region['type'].replace('-', ' ').title()} Area"
        ).add_to(m)
    
    js_script = """
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(function() {
                let layers = document.querySelectorAll(".leaflet-interactive");
                layers.forEach((layer, index) => {
                    let weatherTypes = ['snow-mask', 'rain-mask', 'fog-mask', 'sunny-mask', 'cloudy-mask', 'partly-cloudy-mask', 'thunderstorm-mask'];
                    layer.classList.add(weatherTypes[index % weatherTypes.length]);
                });
            }, 1000); // Delay to allow map to render
        });
    </script>
    """

    m.get_root().html.add_child(folium.Element(js_script))

    return m

# Example usage
if __name__ == "__main__":
    # Create map centered on New York
    center_lat, center_lng = 40.7128, -74.0060
    map_object = create_full_weather_map(center_lat, center_lng)
    map_object.save('full_weather_map.html')