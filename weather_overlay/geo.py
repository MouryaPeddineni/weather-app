import folium
from folium import Element
import json

def create_weather_map():
    # Create a map centered on Bangalore
    bangalore_coords = [12.9716, 77.5946]
    m = folium.Map(location=bangalore_coords, zoom_start=11)
    
    # Define the SVG animation
    svg_animation = """
    <div id="weather-overlay" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); pointer-events: none; opacity: 0.5; z-index: 1000;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">
            <!-- Definitions for reuse -->
            <defs>
                <!-- Cloud shape -->
                <path id="cloud" d="M25,50 Q37.5,35 50,50 Q62.5,35 75,50 Q87.5,35 100,50 L100,65 L25,65 Z" fill="#E6E6E6"/>
                
                <!-- Rain drop -->
                <path id="raindrop" d="M5,0 L8,5 L5,10 L2,5 Z" fill="#4F95FF"/>
            </defs>
            
            <!-- Cloudy Area (Left Side) -->
            <rect x="0" y="0" width="200" height="200" fill="#E8F4F8"/>
            <g>
                <use href="#cloud" x="20" y="20">
                    <animateTransform
                        attributeName="transform"
                        type="translate"
                        dur="4s"
                        values="0,0; 15,0; 0,0"
                        repeatCount="indefinite"/>
                </use>
                <use href="#cloud" x="80" y="50">
                    <animateTransform
                        attributeName="transform"
                        type="translate"
                        dur="6s"
                        values="0,0; -15,0; 0,0"
                        repeatCount="indefinite"/>
                </use>
                <use href="#cloud" x="40" y="80">
                    <animateTransform
                        attributeName="transform"
                        type="translate"
                        dur="5s"
                        values="0,0; 20,0; 0,0"
                        repeatCount="indefinite"/>
                </use>
            </g>
            
            <!-- Rainy Area (Right Side) -->
            <rect x="200" y="0" width="200" height="200" fill="#D6E6F2"/>
            <g>
                <!-- Static clouds -->
                <use href="#cloud" x="220" y="20"/>
                <use href="#cloud" x="280" y="40"/>
                <use href="#cloud" x="240" y="60"/>
                
                <!-- Raindrops with different starting positions -->
                <g>
                    <use href="#raindrop" x="240" y="70">
                        <animateTransform
                            attributeName="transform"
                            type="translate"
                            dur="1s"
                            values="0,0; 0,100"
                            repeatCount="indefinite"/>
                    </use>
                    <use href="#raindrop" x="280" y="50">
                        <animateTransform
                            attributeName="transform"
                            type="translate"
                            dur="1.2s"
                            values="0,0; 0,100"
                            repeatCount="indefinite"/>
                    </use>
                    <use href="#raindrop" x="320" y="80">
                        <animateTransform
                            attributeName="transform"
                            type="translate"
                            dur="0.9s"
                            values="0,0; 0,100"
                            repeatCount="indefinite"/>
                    </use>
                    <use href="#raindrop" x="260" y="90">
                        <animateTransform
                            attributeName="transform"
                            type="translate"
                            dur="1.1s"
                            values="0,0; 0,100"
                            repeatCount="indefinite"/>
                    </use>
                    <use href="#raindrop" x="300" y="60">
                        <animateTransform
                            attributeName="transform"
                            type="translate"
                            dur="1.3s"
                            values="0,0; 0,100"
                            repeatCount="indefinite"/>
                    </use>
                </g>
            </g>
        </svg>
    </div>
    """

    # Add the SVG animation to the map using a custom HTML element
    html = f"""
        <div style="position: relative;">
            {svg_animation}
        </div>
    """
    
    # Create a custom Element and add it to the map
    overlay = Element(html)
    m.get_root().html.add_child(overlay)
    
    return m

# Create and save the map
map_with_animation = create_weather_map()
map_with_animation.save('bangalore_weather_map.html')