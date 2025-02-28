from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import datetime
import time
import cv2
import numpy as np
import base64
from PIL import Image
import io
import os
from tempfile import NamedTemporaryFile
import streamlit as st
import requests


GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
GOOGLE_CSE_ID = "3269dbbc6cdf0482b"
GOOGLE_PLACES_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
OPENWEATHER_API_KEY = "a37be5e437c1d804ad68daaec7139c6c"


def get_weather_icon(condition):
    """Get appropriate weather icon based on condition"""
    icons = {
        'Clear': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="5"/>
            <line x1="12" y1="1" x2="12" y2="3"/>
            <line x1="12" y1="21" x2="12" y2="23"/>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
            <line x1="1" y1="12" x2="3" y2="12"/>
            <line x1="21" y1="12" x2="23" y2="12"/>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
        </svg>''',
        'Clouds': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>
        </svg>''',
        'Rain': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="16" y1="13" x2="16" y2="21"/>
            <line x1="8" y1="13" x2="8" y2="21"/>
            <line x1="12" y1="15" x2="12" y2="23"/>
            <path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"/>
        </svg>''',
        'Snow': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M20 17.58A5 5 0 0 0 18 8h-1.26A8 8 0 1 0 4 16.25"/>
            <line x1="8" y1="16" x2="8.01" y2="16"/>
            <line x1="8" y1="20" x2="8.01" y2="20"/>
            <line x1="12" y1="18" x2="12.01" y2="18"/>
            <line x1="12" y1="22" x2="12.01" y2="22"/>
            <line x1="16" y1="16" x2="16.01" y2="16"/>
            <line x1="16" y1="20" x2="16.01" y2="20"/>
        </svg>''',
        'Sunset': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M17 18a5 5 0 0 0-10 0"/>
            <line x1="12" y1="9" x2="12" y2="2"/>
            <line x1="4.22" y1="10.22" x2="5.64" y2="11.64"/>
            <line x1="1" y1="18" x2="3" y2="18"/>
            <line x1="21" y1="18" x2="23" y2="18"/>
            <line x1="18.36" y1="11.64" x2="19.78" y2="10.22"/>
            <line x1="23" y1="22" x2="1" y2="22"/>
            <polyline points="16 5 12 9 8 5"/>
        </svg>'''
    }
    return icons.get(condition, icons['Sunset'])

def create_weather_hours(current_hour=16):  # 4PM = 16
    """Create array of formatted hours"""
    hours = []
    for i in range(5):
        hour = (current_hour + i) % 24
        if hour == 0:
            formatted = "12AM"
        elif hour < 12:
            formatted = f"{hour}AM"
        elif hour == 12:
            formatted = "12PM"
        else:
            formatted = f"{hour-12}PM"
        hours.append(formatted)
    return hours

def get_formatted_weather(city):
    """
    Fetch weather data from OpenWeather API and format it to match the required structure
    
    Args:
        city (str): Name of the city
        
    Returns:
        list: List of weather condition dictionaries with time, temp, and condition
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'imperial',  # Get temperature in Fahrenheit
        'cnt': 8  # Get next 24 hours of data (3-hour intervals)
    }
    
    try:
        # Get current time for sunset calculation
        current_weather_url = f"http://api.openweathermap.org/data/2.5/weather"
        current_response = requests.get(current_weather_url, params={
            'q': city,
            'appid': OPENWEATHER_API_KEY
        })
        current_data = current_response.json()
        sunset_time = datetime.fromtimestamp(current_data['sys']['sunset'])
        sunset_hour = sunset_time.strftime("%I:%M")  # Format: HH:MM in 12-hour format
        
        # Get forecast data
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None
            
        weather_conditions = []
        for i, item in enumerate(data['list'][:6]):  # Get first 6 time slots
            # Convert timestamp to datetime
            dt = datetime.fromtimestamp(item['dt'])
            
            # Format time in 12-hour format
            time = dt.strftime("%I%p").lstrip('0')  # Remove leading zero
            
            # Get temperature and round to nearest integer
            temp = round(item['main']['temp'])
            
            # Get weather condition
            condition = item['weather'][0]['main']
            
            # Create weather condition entry
            weather_entry = {
                "time": time,
                "temp": temp,
                "condition": condition
            }
            
            # Insert sunset entry if it falls within this time period
            if i > 0 and len(weather_conditions) < 6:
                prev_dt = datetime.fromtimestamp(data['list'][i-1]['dt'])
                if prev_dt.timestamp() <= current_data['sys']['sunset'] <= dt.timestamp():
                    weather_conditions.append({
                        "time": sunset_hour,
                        "temp": temp,  # Use same temp as current period
                        "condition": "Sunset"
                    })
            
            weather_conditions.append(weather_entry)
        
        # Ensure we only have 6 entries
        weather_conditions = weather_conditions[:6]
        
        return weather_conditions
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {str(e)}")
        return None
    except KeyError as e:
        print(f"Error parsing weather data: {str(e)}")
        return None


def get_weather_html(city):
    """Generate weather widget HTML with dynamic data"""
    # Simulated weather data - in production, this would come from your weather API
    weather_conditions = get_formatted_weather(city)
    
    hours = create_weather_hours()
    weather_html = ""
    
    for i, weather in enumerate(weather_conditions):
        icon = get_weather_icon(weather['condition'])
        weather_html += f"""
            <div class="weather-hour">
                <div class="hour-text">{weather['time']}</div>
                <div class="weather-icon">
                    {icon}
                </div>
                <div class="temp-text">{weather['temp']}°</div>
            </div>
        """
    
    return f"""
    <div class="weather-widget">
        <div class="weather-header">
            <div>
                <div class="city-name">{city}</div>
                <div class="current-temp">{weather['time']}</div>
            </div>
            <div class="weather-warning">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="warning-icon">
                    <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
                    <line x1="12" y1="9" x2="12" y2="13"/>
                    <line x1="12" y1="17" x2="12.01" y2="17"/>
                </svg>
                {weather['condition']}
            </div>
        </div>
        <div class="weather-forecast">
            {weather_html}
        </div>
    </div>
    """

# Update the styles in your HTML to include these additional CSS rules:
ADDITIONAL_STYLES = """
.weather-icon {
    margin: 10px 0;
    display: flex;
    justify-content: center;
    align-items: center;
}
.weather-icon svg {
    width: 24px;
    height: 24px;
    stroke: white;
}
.hour-text {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.9);
}
.temp-text {
    font-size: 16px;
    font-weight: 500;
}
.warning-icon {
    vertical-align: middle;
    margin-right: 5px;
}
.city-name {
    font-size: 18px;
    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 5px;
}
.current-temp {
    font-size: 48px;
    font-weight: bold;
    line-height: 1;
}
.weather-warning {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    background: rgba(255,255,255,0.2);
    border-radius: 5px;
    font-size: 14px;
}
"""



def get_popular_places(city):
    """Fetch popular tourist attractions in a city using Google Places API."""
    query = f"top tourist attractions in {city} excluding religious sites"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={GOOGLE_PLACES_API_KEY}&rankby=prominence"

    response = requests.get(url)
    data = response.json()

    if "error_message" in data:
        print(f"⚠️ API Error: {data['error_message']}")
        return None

    places = []
    for place in data.get("results", []):
        name = place.get("name", "Unknown Place")
        places.append({"name": name})
    print(places)
    return places


def get_coordinates(city):
    """Get latitude and longitude for a given city using OpenCage Geocoding API"""
    api_key = "cb40be970fa24926b3b0cb4233b21f1e"
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


def search_image(query):
    """Fetch an image using Google Custom Search API, avoiding googleusercontent.com."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": f"{query}",
        "cx": GOOGLE_CSE_ID,
        "key": GOOGLE_API_KEY,
        "searchType": "image",
        "num": 5,
    }
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "items" in data:
            for item in data["items"]:
                image_url = item["link"]
                if "googleusercontent.com" not in image_url and "maps.wikimedia.com" not in image_url:
                    return image_url
        return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching image: {e}")
        return None


def get_weather(city):
    """Get weather data for a given city using OpenWeather API"""
    OPENWEATHER_API_KEY = "a37be5e437c1d804ad68daaec7139c6c"
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'imperial'
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error getting weather: {str(e)}")
        return None


def create_particle_animation_html(city_coords, place_image_url, city):
    weather_data = get_weather(city)
    if not weather_data:
        return None
    
    # Extract next 5 hours of weather data
    forecasts = weather_data['list'][:5]
    weather_html = get_weather_html(city)
    for i, forecast in enumerate(forecasts):
        temp = round(forecast['main']['temp'])
        time = (i + 4).__str__() + "PM"  # Starting from 4PM
        icon = "☀️" if forecast['weather'][0]['main'] == 'Clear' else "☁️"
        weather_html += f"""
            <div class="weather-hour">
                <div>{time}</div>
                <div>{icon}</div>
                <div>{temp}°</div>
            </div>
        """
    
    lat, lng = get_coordinates(city)
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
            <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
            <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css" />
            <style>
                body {{
                    margin: 0;
                    display: flex;
                    overflow: hidden;
                }}
                #windy {{
                    width: 50%;
                    height: 600px;
                    border-radius: 10px 0 0 10px;
                }}
                .right-container {{
                    width: 50%;
                    height: 600px;
                    display: flex;
                    flex-direction: column;
                }}
                #places-container {{
                    height: 60%;
                    background: black;
                    position: relative;
                    overflow: hidden;
                }}
                #weather-container {{
                    height: 40%;
                    background: #1e88e5;
                    border-radius: 15px;
                    padding: 20px;
                    color: white;
                    font-family: Arial, sans-serif;
                }}
                #place-image {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }}
                .place-title {{
                    position: absolute;
                    bottom: 20px;
                    right: 20px;
                    color: white;
                    background: rgba(0,0,0,0.7);
                    padding: 10px;
                    border-radius: 5px;
                    font-family: Arial, sans-serif;
                }}
                .weather-widget {{
                    display: flex;
                    flex-direction: column;
                    height: 100%;
                }}
                .weather-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 20px;
                }}
                .current-temp {{
                    font-size: 48px;
                    font-weight: bold;
                }}
                .weather-warning {{
                    padding: 5px 10px;
                    background: rgba(255,255,255,0.2);
                    border-radius: 5px;
                }}
                .weather-forecast {{
                    display: flex;
                    justify-content: space-between;
                    margin-top: 20px;
                }}
                .weather-hour {{
                    text-align: center;
                    font-size: 14px;
                }}
                .weather-hour > div {{
                    margin: 5px 0;
                }}
            </style>
        </head>
        <body>
            <div id="windy"></div>
            <div class="right-container">
                <div id="places-container">
                    <img id="place-image" src="{place_image_url}" alt="Popular Place"/>
                    <div class="place-title">Popular Attractions in {city}</div>
                </div>
                <div id="weather-container">
                    <div class="weather-widget">
                        <div class="weather-header">
                            <div>
                                <div>{city}</div>
                                <div class="current-temp">47°</div>
                            </div>
                            <div class="weather-warning">Winter storm warning</div>
                        </div>
                        <div class="weather-forecast">
                            {weather_html}
                        </div>
                    </div>
                </div>
            </div>
            <script>
                const options = {{
                    key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y',
                    verbose: true,
                    lat: {lat},
                    lon: {lng},
                    zoom: 8
                }};

                windyInit(options, windyAPI => {{
                    const {{ map, overlays, broadcast }} = windyAPI;
                    const windMetric = overlays.wind.metric;
                    overlays.wind.setMetric('bft');
                    
                    const marker = L.marker([{lat}, {lng}], {{
                        title: '{city}'
                    }}).addTo(map);
                }});
            </script>
        </body>
    </html>
    """

# Rest of the functions (get_coordinates, get_popular_places, search_image) remain the same

def create_particle_animation_html(city_coords, place_image_url, city):
    # Get real-time weather data
    weather_data = get_weather(city)
    if not weather_data:
        return None

    # Extract current weather and forecasts
    current_weather = weather_data["list"][0]
    current_temp = round(current_weather["main"]["temp"])
    current_condition = current_weather["weather"][0]["main"]

    # Get next 5 forecasts
    forecasts = weather_data["list"][:5]
    weather_html = ""

    for forecast in forecasts:
        temp = round(forecast["main"]["temp"])
        time = forecast["dt_txt"].split()[1][:5]  # Extract hour:minute
        condition = forecast["weather"][0]["description"].capitalize()  # Use full description
        icon = get_weather_icon(condition)

        weather_html += f"""
            <div class="weather-hour">
                <div class="hour-text">{time}</div>
                <div class="weather-icon">
                    {icon}
                </div>
                <div class="temp-text">{temp}°</div>
                <div class="condition-text">{condition}</div>
            </div>
        """

    
    lat, lng = get_coordinates(city)
    
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
            <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
            <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css" />
            <style>
                body {{
                    margin: 0;
                    display: flex;
                    overflow: hidden;
                    height: 100vh;
                    width: 100vw;
                }}
                #windy {{
                    width: 50%;
                    height: 100vh;
                }}
                .right-container {{
                    width: 50%;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                }}
                #places-container {{
                    height: 50%;
                    position: relative;
                    overflow: hidden;
                }}
                #weather-container {{
                    height: 50%;
                    background: linear-gradient(135deg, #1e88e5, #1565c0);
                    padding: 20px;
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    flex-direction: column;
                }}
                #place-image {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }}
                .place-title {{
                    position: absolute;
                    bottom: 20px;
                    right: 20px;
                    color: white;
                    background: rgba(0,0,0,0.7);
                    padding: 10px;
                    border-radius: 5px;
                    font-family: Arial, sans-serif;
                }}
                .weather-widget {{
                    display: flex;
                    flex-direction: column;
                    height: 100%;
                    justify-content: space-between;
                }}
                .weather-header {{
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-start;
                }}
                .city-name {{
                    font-size: 24px;
                    margin-bottom: 5px;
                }}
                .current-temp {{
                    font-size: 64px;
                    font-weight: bold;
                    line-height: 1;
                }}
                .weather-warning {{
                    padding: 8px 12px;
                    background: rgba(255,255,255,0.2);
                    border-radius: 5px;
                    display: flex;
                    align-items: center;
                    gap: 5px;
                }}
                .weather-forecast {{
                    display: flex;
                    justify-content: space-between;
                    padding: 20px 0;
                }}
                .weather-hour {{
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 10px;
                }}
                .weather-icon svg {{
                    width: 30px;
                    height: 30px;
                    stroke: white;
                }}
                .hour-text {{
                    font-size: 16px;
                    color: rgba(255,255,255,0.9);
                }}
                .temp-text {{
                    font-size: 18px;
                    font-weight: 500;
                }}
                @media (max-width: 1200px) {{
                    body {{
                        flex-direction: column;
                    }}
                    #windy, .right-container {{
                        width: 100%;
                        height: 50vh;
                    }}
                }}
            </style>
        </head>
        <body>
            <div id="windy"></div>
            <div class="right-container">
                <div id="places-container">
                    <img id="place-image" src="{place_image_url}" alt="Popular Place"/>
                </div>
                <div id="weather-container">
                    <div class="weather-widget">
                        <div class="weather-header">
                            <div>
                                <div class="city-name">{city}</div>
                                <div class="current-temp">{current_temp}°</div>
                            </div>
                            <div class="weather-warning">
                                {get_weather_icon(condition)}
                                {current_condition}
                            </div>
                        </div>
                        <div class="weather-forecast">
                            {weather_html}
                        </div>
                    </div>
                </div>
            </div>
            <script>
                const options = {{
                    key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y',
                    verbose: true,
                    lat: {lat},
                    lon: {lng},
                    zoom: 8
                }};

                windyInit(options, windyAPI => {{
                    const {{ map, overlays }} = windyAPI;
                    overlays.wind.setMetric('bft');
                    L.marker([{lat}, {lng}], {{
                        title: '{city}'
                    }}).addTo(map);
                }});
            </script>
        </body>
    </html>
    """

def capture_animation_frames(city="Asheville", duration_seconds=3, fps=30):
    """
    Capture frames from the particle animation using Selenium in headless mode
    """
    # Get screen resolution
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--start-maximized')
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Get screen dimensions
        screen_width = driver.execute_script('return screen.width;')
        screen_height = driver.execute_script('return screen.height;')
        
        chrome_options.add_argument(f'--window-size={screen_width},{screen_height}')
        driver = webdriver.Chrome(options=chrome_options)
        
        places = get_popular_places(city)
        if not places or len(places) == 0:
            print("No places found!")
            return
        
        place_image_url = search_image(f"{places[0]['name']} {city}")
        if not place_image_url:
            print("No image found!")
            return
        
        with NamedTemporaryFile(suffix='.html', mode='w', delete=False) as f:
            html_content = create_particle_animation_html(None, place_image_url, city)
            f.write(html_content)
            temp_html_path = f.name
        
        driver.get(f'file://{temp_html_path}')
        time.sleep(2)
        
        frames = []
        num_frames = int(duration_seconds * fps)
        
        print("Capturing frames...")
        for i in range(num_frames):
            screenshot = driver.get_screenshot_as_base64()
            img_data = base64.b64decode(screenshot)
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((screen_width, screen_height))
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            frames.append(frame)
            
            time.sleep(1/fps)
            if i % 10 == 0:
                print(f"Captured frame {i+1}/{num_frames}")
        
        # Save video with screen dimensions
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('weather_places_animation.mp4', fourcc, fps, (screen_width, screen_height))
        
        for frame in frames:
            out.write(frame)
        
        out.release()
        os.remove(temp_html_path)
        
        print("Video saved as weather_places_animation.mp4")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    capture_animation_frames(city="Bengaluru", duration_seconds=3, fps=20)