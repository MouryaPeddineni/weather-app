import folium
import numpy as np
import pandas as pd
from folium import plugins

class WeatherConditionMap:
    def __init__(self, center_lat=0, center_lng=0, zoom_start=3):
        self.map = folium.Map(
            location=[center_lat, center_lng],
            zoom_start=zoom_start,
            tiles='cartodbpositron'
        )
        self.add_custom_css()
    
    def add_custom_css(self):
        """Add custom CSS for weather condition styling"""
        custom_css = """
            <style>
            .weather-icon {
                position: relative;
                width: 40px;
                height: 40px;
                border-radius: 50%;
            }
            
            .sunny {
                background: radial-gradient(circle at 50% 50%, 
                    rgba(255, 165, 0, 0.8),
                    rgba(255, 165, 0, 0.4));
            }
            
            .cloudy {
                background: radial-gradient(circle at 50% 50%, 
                    rgba(169, 169, 169, 0.8),
                    rgba(169, 169, 169, 0.4));
            }
            
            .rainy {
                background: radial-gradient(circle at 50% 50%, 
                    rgba(0, 0, 255, 0.6),
                    rgba(0, 0, 255, 0.3));
            }
            
            .snow {
                background: radial-gradient(circle at 50% 50%, 
                    rgba(255, 255, 255, 0.8),
                    rgba(255, 255, 255, 0.4));
                border: 1px solid rgba(200, 200, 200, 0.5);
            }
            
            .thunderstorm {
                background: radial-gradient(circle at 50% 50%, 
                    rgba(75, 0, 130, 0.8),
                    rgba(75, 0, 130, 0.4));
            }
            
            .legend-item {
                margin-bottom: 5px;
                display: flex;
                align-items: center;
            }
            
            .legend-color {
                width: 20px;
                height: 20px;
                margin-right: 5px;
                border-radius: 50%;
            }
            </style>
        """
        self.map.get_root().html.add_child(folium.Element(custom_css))

    def get_weather_style(self, condition):
        """Get the appropriate CSS class and color for weather condition"""
        styles = {
            'sunny': {
                'class': 'sunny',
                'color': 'orange',
                'icon': '☀️'
            },
            'cloudy': {
                'class': 'cloudy',
                'color': '#A9A9A9',
                'icon': '☁️'
            },
            'rainy': {
                'class': 'rainy',
                'color': '#4169E1',
                'icon': '🌧️'
            },
            'snow': {
                'class': 'snow',
                'color': '#FFFFFF',
                'icon': '❄️'
            },
            'thunderstorm': {
                'class': 'thunderstorm',
                'color': '#4B0082',
                'icon': '⛈️'
            }
        }
        return styles.get(condition, styles['sunny'])

    def add_weather_conditions(self, weather_data):
        """Add weather conditions to the map"""
        weather_layer = folium.FeatureGroup(name='Weather Conditions')
        
        for _, row in weather_data.iterrows():
            style = self.get_weather_style(row['condition'])
            
            # Create weather marker with condition-specific styling
            html = f"""
                <div class='weather-icon {style["class"]}'>
                    <div style='position: absolute; 
                               top: 50%; 
                               left: 50%; 
                               transform: translate(-50%, -50%);
                               font-size: 20px;'>
                        {style['icon']}
                    </div>
                </div>
            """
            
            # Add popup content
            popup_html = f"""
                <div style='font-family: Arial; padding: 5px;'>
                    <h4>{row['city']}</h4>
                    <p>Condition: {row['condition'].title()}</p>
                    <p>Temperature: {row['temperature']}°C</p>
                </div>
            """
            
            folium.Marker(
                location=[row['lat'], row['lon']],
                icon=folium.DivIcon(
                    html=html,
                    icon_size=(40, 40),
                    icon_anchor=(20, 20)
                ),
                popup=folium.Popup(popup_html, max_width=200)
            ).add_to(weather_layer)
        
        weather_layer.add_to(self.map)

    def add_legend(self):
        """Add a legend showing weather conditions"""
        legend_html = """
            <div style="position: fixed; 
                        bottom: 50px; right: 50px; 
                        border: 2px solid grey; 
                        z-index: 9999; 
                        background-color: white;
                        padding: 10px;
                        border-radius: 5px;
                        font-size: 14px;">
                <p style="margin-bottom: 10px"><strong>Weather Conditions</strong></p>
                <div class="legend-item">
                    <div class="legend-color sunny"></div>
                    <span>Sunny</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color cloudy"></div>
                    <span>Cloudy</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color rainy"></div>
                    <span>Rainy</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color snow"></div>
                    <span>Snow</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color thunderstorm"></div>
                    <span>Thunderstorm</span>
                </div>
            </div>
        """
        self.map.get_root().html.add_child(folium.Element(legend_html))

# Example usage
if __name__ == "__main__":
    # Sample weather data for US cities
    weather_data = pd.DataFrame({
        'city': ['New York', 'Chicago', 'Miami', 'Denver', 'Los Angeles'],
        'lat': [40.7128, 41.8781, 25.7617, 39.7392, 34.0522],
        'lon': [-74.0060, -87.6298, -80.1918, -104.9903, -118.2437],
        'condition': ['sunny', 'snow', 'thunderstorm', 'cloudy', 'sunny'],
        'temperature': [25, -2, 30, 15, 28]
    })
    
    # Create map centered on US
    weather_map = WeatherConditionMap(center_lat=39.8283, center_lng=-98.5795, zoom_start=4)
    
    # Add weather conditions
    weather_map.add_weather_conditions(weather_data)
    weather_map.add_legend()
    
    # Save the map
    weather_map.map.save('weather_conditions.html')