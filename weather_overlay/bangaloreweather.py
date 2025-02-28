import folium
from folium import Element

def create_weather_map():
    # Create a satellite map centered on Bangalore
    bangalore_coords = [12.9716, 77.5946]

    m = folium.Map(location=bangalore_coords, zoom_start=10, tiles="CartoDB dark_matter")

    svg_animation = """
        <div class="weather-container">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">
                <defs>
                    <path id="cloud-shape" d="M25,50 Q37.5,35 50,50 Q62.5,35 75,50 Q87.5,35 100,50 L100,65 L25,65 Z" 
                          fill="#FFFFFF" stroke="#666666" stroke-width="2"/>
                    <path id="rain-drop" d="M5,0 L8,5 L5,10 L2,5 Z" 
                          fill="#0066FF" stroke="#0044CC" stroke-width="1"/>
                </defs>

                <g class="moving-clouds">
                    <use href="#cloud-shape" x="20" y="20">
                        <animate attributeName="x" from="20" to="35" dur="4s" repeatCount="indefinite"/>
                    </use>
                    <use href="#cloud-shape" x="80" y="50">
                        <animate attributeName="x" from="80" to="65" dur="6s" repeatCount="indefinite"/>
                    </use>
                </g>

                <g class="raindrops">
                    <use href="#rain-drop" x="240" y="70">
                        <animate attributeName="y" from="70" to="170" dur="1s" repeatCount="indefinite"/>
                    </use>
                    <use href="#rain-drop" x="280" y="50">
                        <animate attributeName="y" from="50" to="150" dur="1.2s" repeatCount="indefinite"/>
                    </use>
                </g>
            </svg>
        </div>
    """

    # Add the animation to the map using folium.DivIcon
    folium.Marker(
        bangalore_coords,
        icon=folium.DivIcon(
            html=svg_animation,
            icon_size=(400, 200),
            icon_anchor=(200, 100),
            class_name='weather-animation'
        )
    ).add_to(m)
    
    css = """
        <style>
        .weather-container {
            position: absolute;
            width: 400px;
            height: 200px;
            pointer-events: none;
        }
        </style>
    """
    m.get_root().header.add_child(Element(css))

    wind_js = """
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
        <script src="https://unpkg.com/wind-gl@latest/dist/wind-gl.min.js"></script>

        <script>
            document.addEventListener("DOMContentLoaded", function () {
                // Delay to ensure the map loads
                setTimeout(() => {
                    var leafletMap = L.map(document.querySelector(".leaflet-container"));

                    var windLayer = new WindGL({
                        map: leafletMap,
                        windOptions: {
                            velocityScale: 0.02, 
                            particleAge: 100,
                            particleMultiplier: 1.5,
                            lineWidth: 1.2
                        }
                    });

                    // Fetch wind data
                    fetch('https://raw.githubusercontent.com/visualize-admin/wind-gl/master/examples/wind-data.json')
                    .then(response => response.json())
                    .then(data => {
                        windLayer.setData(data);
                    })
                    .catch(error => console.error("Wind Data Load Error: ", error));

                    // Add WindGL Layer
                    windLayer.addTo(leafletMap);
                }, 1000);  // Ensure Folium map loads first
            });
        </script>
    """

    # Inject the JavaScript into the map
    m.get_root().html.add_child(Element(wind_js))

    return m

# Create and save the map
map_with_animation = create_weather_map()
map_with_animation.save('bangalore_weather_map.html')
