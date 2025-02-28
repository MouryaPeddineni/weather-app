# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# import time
# import cv2
# import numpy as np
# import base64
# from PIL import Image
# import io
# import os
# from tempfile import NamedTemporaryFile
# import streamlit as st
# import requests

# def get_coordinates(city):
#     """Get latitude and longitude for a given city using OpenCage Geocoding API"""
#     api_key = "cb40be970fa24926b3b0cb4233b21f1e"  # Replace with your OpenCage API key
#     base_url = "https://api.opencagedata.com/geocode/v1/json"
    
#     params = {
#         'q': city,
#         'key': api_key,
#         'limit': 1
#     }
    
#     try:
#         response = requests.get(base_url, params=params)
#         data = response.json()
#         if data['results']:
#             lat = data['results'][0]['geometry']['lat']
#             lng = data['results'][0]['geometry']['lng']
#             return lat, lng
#         return None, None
#     except Exception as e:
#         st.error(f"Error getting coordinates: {str(e)}")
#         return None, None
    

# def create_particle_animation_html(city_coords):
#     lat, lng = get_coordinates("Bengaluru")
#     return f"""
#    <!DOCTYPE html>
#                 <html>
#                     <head>
#                         <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
#                         <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
#                         <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
#                         <link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css" />
#                         <style>
#                             #windy {{
#                                 width: 100%;
#                                 height: 600px;
#                                 border-radius: 10px;
#                             }}
#                             .marker-pin {{
#                                 width: 30px;
#                                 height: 30px;
#                                 border-radius: 50% 50% 50% 0;
#                                 background: #c30b82;
#                                 position: absolute;
#                                 transform: rotate(-45deg);
#                                 left: 50%;
#                                 top: 50%;
#                                 margin: -15px 0 0 -15px;
#                             }}
#                         </style>
#                     </head>
#                     <body>
#                         <div id="windy"></div>
#                         <script>
#                             const options = {{
#                                 key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y',
#                                 verbose: true,
#                                 lat: {lat},
#                                 lon: {lng},
#                                 zoom: 8
#                             }};

#                             windyInit(options, windyAPI => {{
#                                 const {{ map, overlays, broadcast }} = windyAPI;
#                                 const windMetric = overlays.wind.metric;
#                                 overlays.wind.setMetric('bft');
                                
#                                 // Add marker for Bengaluru
#                                 const marker = L.marker([{lat}, {lng}], {{
#                                     title: 'Bengaluru'
#                                 }}).addTo(map);
                                
#                                 // Add popup to marker
#                                 // marker.bindPopup('<b>Bengaluru</b><br>Weather visualization').openPopup();
#                             }});
#                         </script>
#                     </body>
#                 </html>
#     """

# def capture_animation_frames(duration_seconds=3, fps=30):
#     """
#     Capture frames from the particle animation using Selenium in headless mode
#     """
#     width, height = 800, 600
    
#     # Set up Chrome options for headless mode
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument(f'--window-size={width},{height}')
    
#     # Initialize webdriver
#     driver = webdriver.Chrome(options=chrome_options)
    
#     try:
#         # Create temporary HTML file
#         with NamedTemporaryFile(suffix='.html', mode='w', delete=False) as f:
#             html_content = create_particle_animation_html(None)
#             f.write(html_content)
#             temp_html_path = f.name
        
#         # Navigate to the HTML file
#         driver.get(f'file://{temp_html_path}')
#         time.sleep(1)  # Wait for animation to start
        
#         # Prepare frames list
#         frames = []
#         num_frames = int(duration_seconds * fps)
        
#         print("Capturing frames...")
#         for i in range(num_frames):
#             # Get screenshot as base64
#             screenshot = driver.get_screenshot_as_base64()
#             img_data = base64.b64decode(screenshot)
#             img = Image.open(io.BytesIO(img_data))
            
#             # Ensure correct size
#             img = img.resize((width, height))
            
#             # Convert to opencv format
#             frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#             frames.append(frame)
            
#             time.sleep(1/fps)
#             if i % 10 == 0:
#                 print(f"Captured frame {i+1}/{num_frames}")
        
#         print("Writing video...")
        
#         # Save as uncompressed AVI first
#         temp_avi = 'temp_output.avi'
#         fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#         out = cv2.VideoWriter(temp_avi, fourcc, fps, (width, height))
        
#         for frame in frames:
#             out.write(frame)
#         out.release()
        
#         print("Converting to MP4...")
        
#         # Convert to MP4 using OpenCV
#         input_video = cv2.VideoCapture(temp_avi)
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         out = cv2.VideoWriter('particle_animation.mp4', fourcc, fps, (width, height))
        
#         while True:
#             ret, frame = input_video.read()
#             if not ret:
#                 break
#             out.write(frame)
        
#         input_video.release()
#         out.release()
        
#         # Cleanup
#         os.remove(temp_avi)
#         os.remove(temp_html_path)
        
#         print("Video saved as particle_animation.mp4")
        
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     capture_animation_frames(duration_seconds=3, fps=30)


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# import time
# import cv2
# import numpy as np
# import base64
# from PIL import Image
# import io
# import os
# from tempfile import NamedTemporaryFile
# import streamlit as st
# import requests

# # API Keys
# GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
# GOOGLE_CSE_ID = "3269dbbc6cdf0482b"
# GOOGLE_PLACES_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
# OPENWEATHER_API_KEY = "a37be5e437c1d804ad68daaec7139c6c"

# def get_coordinates(city):
#     """Get latitude and longitude for a given city using OpenCage Geocoding API"""
#     api_key = "cb40be970fa24926b3b0cb4233b21f1e"
#     base_url = "https://api.opencagedata.com/geocode/v1/json"
    
#     params = {
#         'q': city,
#         'key': api_key,
#         'limit': 1
#     }
    
#     try:
#         response = requests.get(base_url, params=params)
#         data = response.json()
#         if data['results']:
#             lat = data['results'][0]['geometry']['lat']
#             lng = data['results'][0]['geometry']['lng']
#             return lat, lng
#         return None, None
#     except Exception as e:
#         st.error(f"Error getting coordinates: {str(e)}")
#         return None, None

# def get_popular_places(city):
#     """Fetch popular tourist attractions in a city using Google Places API."""
#     query = f"top tourist attractions in {city} excluding religious sites"
#     url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={GOOGLE_PLACES_API_KEY}&rankby=prominence"

#     response = requests.get(url)
#     data = response.json()

#     if "error_message" in data:
#         print(f"⚠️ API Error: {data['error_message']}")
#         return None

#     places = []
#     for place in data.get("results", []):
#         name = place.get("name", "Unknown Place")
#         places.append({"name": name})
#     print(places)
#     return places

# def search_image(query):
#     """Fetch an image using Google Custom Search API, avoiding googleusercontent.com."""
#     url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         "q": f"{query}",
#         "cx": GOOGLE_CSE_ID,
#         "key": GOOGLE_API_KEY,
#         "searchType": "image",
#         "num": 5,
#     }
#     headers = {"User-Agent": "Mozilla/5.0"}

#     try:
#         response = requests.get(url, params=params, headers=headers)
#         response.raise_for_status()
#         data = response.json()

#         if "items" in data:
#             for item in data["items"]:
#                 image_url = item["link"]
#                 if "googleusercontent.com" not in image_url and "maps.wikimedia.com" not in image_url:
#                     return image_url
#         return None
#     except requests.exceptions.RequestException as e:
#         print(f"⚠️ Error fetching image: {e}")
#         return None

# def create_particle_animation_html(city_coords, place_image_url):
#     lat, lng = get_coordinates("Bengaluru")
#     return f"""
#    <!DOCTYPE html>
#                 <html>
#                     <head>
#                         <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no"/>
#                         <script src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
#                         <script src="https://api.windy.com/assets/map-forecast/libBoot.js"></script>
#                         <link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css" />
#                         <style>
#                             body {{
#                                 margin: 0;
#                                 display: flex;
#                                 overflow: hidden;
#                             }}
#                             #windy {{
#                                 width: 50%;
#                                 height: 600px;
#                                 border-radius: 10px 0 0 10px;
#                             }}
#                             #places-container {{
#                                 width: 50%;
#                                 height: 100vh;
#                                 background: black;
#                                 display: flex;
#                                 align-items: center;
#                                 justify-content: center;
#                                 overflow: hidden;
#                             }}
                            # #place-image {{
                            #     width: 100%;
                            #     height: 100%;
                            #     object-fit: cover;
                            # }}
#                             .place-title {{
#                                 position: absolute;
#                                 bottom: 20px;
#                                 right: 20px;
#                                 color: white;
#                                 background: rgba(0,0,0,0.7);
#                                 padding: 10px;
#                                 border-radius: 5px;
#                                 font-family: Arial, sans-serif;
#                             }}
#                         </style>
#                     </head>
#                     <body>
#                         <div id="windy"></div>
#                         <div id="places-container">
#                             <img id="place-image" src="{place_image_url}" alt="Popular Place"/>
#                             <div class="place-title">Popular Attractions in Bengaluru</div>
#                         </div>
#                         <script>
#                             const options = {{
#                                 key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y',
#                                 verbose: true,
#                                 lat: {lat},
#                                 lon: {lng},
#                                 zoom: 8
#                             }};

#                             windyInit(options, windyAPI => {{
#                                 const {{ map, overlays, broadcast }} = windyAPI;
#                                 const windMetric = overlays.wind.metric;
#                                 overlays.wind.setMetric('bft');
                                
#                                 const marker = L.marker([{lat}, {lng}], {{
#                                     title: 'Bengaluru'
#                                 }}).addTo(map);
#                             }});
#                         </script>
#                     </body>
#                 </html>
#     """

# def capture_animation_frames(duration_seconds=3, fps=30):
#     """
#     Capture frames from the particle animation using Selenium in headless mode
#     """
#     width, height = 1600, 600  # Doubled width to accommodate split screen
    
#     # Get popular places and their images
#     places = get_popular_places("Chennai")
#     if not places or len(places) == 0:
#         print("No places found!")
#         return
    
#     # Get image for the first place
#     place_image_url = search_image(f"{places[0]['name']} Bengaluru")
#     if not place_image_url:
#         print("No image found!")
#         return
    
#     # Set up Chrome options for headless mode
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument(f'--window-size={width},{height}')
    
#     # Initialize webdriver
#     driver = webdriver.Chrome(options=chrome_options)
    
#     try:
#         # Create temporary HTML file
#         with NamedTemporaryFile(suffix='.html', mode='w', delete=False) as f:
#             html_content = create_particle_animation_html(None, place_image_url)
#             f.write(html_content)
#             temp_html_path = f.name
        
#         # Navigate to the HTML file
#         driver.get(f'file://{temp_html_path}')
#         time.sleep(2)  # Increased wait time for both map and image to load
        
#         # Prepare frames list
#         frames = []
#         num_frames = int(duration_seconds * fps)
        
#         print("Capturing frames...")
#         for i in range(num_frames):
#             # Get screenshot as base64
#             screenshot = driver.get_screenshot_as_base64()
#             img_data = base64.b64decode(screenshot)
#             img = Image.open(io.BytesIO(img_data))
            
#             # Ensure correct size
#             img = img.resize((width, height))
            
#             # Convert to opencv format
#             frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#             frames.append(frame)
            
#             time.sleep(1/fps)
#             if i % 10 == 0:
#                 print(f"Captured frame {i+1}/{num_frames}")
        
#         print("Writing video...")
        
#         # Save as uncompressed AVI first
#         temp_avi = 'temp_output.avi'
#         fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#         out = cv2.VideoWriter(temp_avi, fourcc, fps, (width, height))
        
#         for frame in frames:
#             out.write(frame)
#         out.release()
        
#         print("Converting to MP4...")
        
#         # Convert to MP4 using OpenCV
#         input_video = cv2.VideoCapture(temp_avi)
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         out = cv2.VideoWriter('particle_animation.mp4', fourcc, fps, (width, height))
        
#         while True:
#             ret, frame = input_video.read()
#             if not ret:
#                 break
#             out.write(frame)
        
#         input_video.release()
#         out.release()
        
#         # Cleanup
#         os.remove(temp_avi)
#         os.remove(temp_html_path)
        
#         print("Video saved as particle_animation.mp4")
        
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     capture_animation_frames(duration_seconds=3, fps=30)



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
from google.cloud import translate_v2 as translate
from langchain_google_genai import ChatGoogleGenerativeAI
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip


GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
GOOGLE_CSE_ID = "3269dbbc6cdf0482b"
GOOGLE_PLACES_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
OPENWEATHER_API_KEY = "a37be5e437c1d804ad68daaec7139c6c"
GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nc25572_mourya/Downloads/ttsaudio-449211-16297ceac279.json"
translator_client = translate.Client()

# Configure Google Gemini
chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, api_key=GEMINI_API_KEY)

def get_greeting():
    """Return appropriate greeting based on time of day"""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 16:
        return "Good afternoon!"
    else:
        return "Good evening!"


def translate_text_google(text, target_lang):
    """Translates text using Google Cloud Translation API."""
    if target_lang == "en":
        return text
    try:
        result = translator_client.translate(text, target_language=target_lang)
        return result["translatedText"]
    except Exception as e:
        print(f"⚠️ Google Translation failed: {e}")
        return text
    

def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
    """Generate weather advice using AI"""
    hour = datetime.datetime.now().hour
    
    hour = hour%12
    
    prompt = f"""
    Do not give any greeting.
    You are a friendly weather advisor. Generate a short, engaging weather report for {city}.
    Current conditions: Temperature: {temp}°C, Weather: {condition}, Time: {hour}
    Focus on current conditions and relevant advice. Keep it natural and conversational.
    Limit the response to 2-3 sentences maximum.
    """

    response = chat_model.predict(prompt).strip()
    translated_response = translate_text_google(response, lang)
    
    greeting = translate_text_google(get_greeting(), lang) if is_first_city else ""
    audio_text = f"{greeting} {translated_response}".strip()
    
    return audio_text


def generate_weather_voice_report(city, lang="en"):
    """Generate voice report for weather"""
    try:
        weather_data = get_weather(city)
        if not weather_data:
            return None
            
        current_weather = weather_data["list"][0]
        temp = round(current_weather["main"]["temp"])
        temp = round((temp - 32) * 5 / 9)
        condition = current_weather["weather"][0]["main"]
        
        audio_text = generate_weather_advice(
            city, temp, condition, lang, is_first_city=True
        )

        API_KEY = "sk_f4a05ebd07348b044d67fe600efd4afc8626877dcad632ac"
        text = audio_text
        voice_id = "JBFqnCBsd6RMkjVDRZzb"

        headers = {
            "Content-Type": "application/json",
            "xi-api-key": API_KEY
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8
            }
        }

        response = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}", json=data, headers=headers)

        if response.status_code == 200:
            with open(f"{city}_weather_audio.mp3", "wb") as file:
                file.write(response.content)
            print("Audio file saved as output.mp3")
        else:
            print("Error:", response.json())

        return f"{city}_weather_audio.mp3"
    except Exception as e:
        print(f"Error generating voice report: {e}")
        return None
    

def get_weather_icon(condition):
    """Get appropriate weather icon based on condition"""
    icons = {
        'Clear': '/Users/nc25572_mourya/Desktop/sunny1.jpg',
        'Clouds': '/Users/nc25572_mourya/Desktop/sunny1.jpg',
        'Rain': '/Users/nc25572_mourya/Desktop/sunny1.jpg',
        'Snow': '/Users/nc25572_mourya/Desktop/sunny1.jpg',
        'Sunset': '/Users/nc25572_mourya/Desktop/sunny1.jpg'
    }
    return icons.get(condition, icons['Sunset'])

def create_weather_hours(current_hour=16):
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
            temp = round((temp - 32) * 5 / 9)
            
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
        icon = get_weather_icon("Rain")
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
    # """Fetch an image using Google Custom Search API, avoiding googleusercontent.com."""
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

        print(data)

        if "items" in data:
            for item in data["items"]:
                image_url = item["link"]
                print(image_url)
                if "googleusercontent.com" not in image_url and "maps.wikimedia.com" not in image_url:
                    return image_url
        return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching image: {e}")
        return None
    return "/Users/nc25572_mourya/Desktop/nashik.jpg"


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


def create_particle_animation_html(city_coords, place_image_url, city, duration):
    """Generate HTML for weather animation with specified duration"""
    weather_data = get_weather(city)
    if not weather_data:
        return None

    current_weather = weather_data["list"][0]
    current_temp = round(current_weather["main"]["temp"])
    current_temp = round((current_temp - 32) * 5 / 9)
    current_condition = current_weather["weather"][0]["main"]

    forecasts = weather_data["list"][:5]
    weather_html = ""

    for forecast in forecasts:
        temp = round(forecast["main"]["temp"])
        temp = round((temp - 32) * 5 / 9)
        time = forecast["dt_txt"].split()[1][:5]
        condition = forecast["weather"][0]["description"].capitalize()
        icon = get_weather_icon(forecast["weather"][0]["main"])

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
                }}
                /* Left side: map takes 50% width and full viewport height */
                #windy {{
                    width: 50%;
                    height: 100vh;
                    border-radius: 10px 0 0 10px;
                }}
                /* Right side container takes the other 50% of the width and full height */
                .right-container {{
                    width: 50%;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                }}
                /* Top half: places container takes 50% height of the right side */
                #places-container {{
                    height: 60%;
                    background: black;
                    position: relative;
                    overflow: hidden;
                }}
                /* Bottom half: weather container takes the remaining 50% */
                #weather-container {{
                    height: 40%;
                    background: #1e88e5;
                    border-radius: 0 10px 10px 0;
                    padding: 20px;
                    color: white;
                    font-family: Arial, sans-serif;
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
                #place-image {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
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
                .leaflet-marker-icon {{
                    transform: scale(1.5); /* Increase size */
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
                                <div>{city}</div>
                                <div class="current-temp">{current_temp}°</div>
                            </div>
                            <div class="weather-warning">{current_condition}</div>
                        </div>
                        <div class="weather-forecast">
                            {weather_html}
                        </div>
                    </div>
                </div>
            </div>
            <script>
                let windyInstance = null;
                
                const initWindy = () => {{
                    if (windyInstance) {{
                        return; // Don't reinitialize if already exists
                    }}
                    
                    const options = {{
                        key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y',
                        verbose: false,
                        lat: {lat},
                        lon: {lng},
                        zoom: 8,
                        timestamp: Date.now(),
                        disableWebGL: true,
                        maxFrameRate: 30
                    }};

                    windyInit(options, windyAPI => {{
                        windyInstance = windyAPI;
                        const {{ map, overlays, broadcast }} = windyAPI;
                        overlays.wind.setMetric('bft');
                        
                        const largeIcon = L.icon({{
                            iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
                            iconSize: [60, 80],  // Size of the icon [width, height]
                            iconAnchor: [17, 55],  // Point of the icon which will correspond to marker's location
                            popupAnchor: [0, -80],  // Point from which the popup should open relative to the iconAnchor
                            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
                            shadowSize: [41, 41],
                            shadowAnchor: [12, 41]
                        }});

                        const marker = L.marker([{lat}, {lng}], {{
                            icon: largeIcon,
                            title: '{city}'
                        }}).addTo(map);
                        
                        // Set animation duration
                        setTimeout(() => {{
                            broadcast.fire('resetAnimation');
                        }}, {duration * 1000});
                    }});
                }};

                // Initialize Windy only once
                initWindy();
            </script>
        </body>
    </html>
    """


def create_weather_video(city, lang="en", fps=30):
    """Create weather video with voice narration"""
    try:
        # Generate voice report first to get audio duration
        audio_file = generate_weather_voice_report(city, lang)
        if not audio_file:
            print("Failed to generate voice report")
            return None
            
        # Get audio duration
        audio_clip = AudioFileClip(audio_file)
        duration_seconds = audio_clip.duration
        audio_clip.close()

        # Set up Chrome options for video capture
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--force-gpu-mem-available-mb=1024')
        
        service = Service()
        driver = webdriver.Chrome(options=chrome_options, service=service)
        
        try:
            # Get screen dimensions
            screen_width = 1920  # Fixed width for consistency
            screen_height = 1080  # Fixed height for consistency
            
            # Update window size
            driver.set_window_size(screen_width, screen_height)
            
            # Get place image
            places = get_popular_places(city)
            if not places or len(places) == 0:
                print("No places found!")
                return None
            
            place_image_url = search_image(f"{places[0]['name']}")
            if not place_image_url:
                print("No image found!")
                return None
            
            # Create temporary HTML file with specified duration
            with NamedTemporaryFile(suffix='.html', mode='w', delete=False) as f:
                html_content = create_particle_animation_html(None, place_image_url, city, duration_seconds)
                f.write(html_content)
                temp_html_path = f.name
            
            # Load page and wait for initialization
            driver.get(f'file://{temp_html_path}')
            time.sleep(3)  # Wait for Windy to initialize
            
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

                if i%100==0:
                    frame_filename = f"frame_{i+100}.png"
                    img.save(frame_filename)
                
                time.sleep(1/fps)
                if i % 10 == 0:
                    print(f"Captured frame {i+1}/{num_frames}")
            
            # Save initial video
            temp_video = 'temp_weather_video.mp4'
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(temp_video, fourcc, fps, (screen_width, screen_height))
            
            for frame in frames:
                out.write(frame)
            out.release()
            
            # Combine video with audio
            print("Combining video and audio...")
            video_clip = VideoFileClip(temp_video)
            audio_clip = AudioFileClip(audio_file)
            
            final_clip = video_clip.set_audio(audio_clip)
            output_file = f'weather_report_{city.lower()}_with_audio.mp4'
            final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
            
            # Cleanup
            video_clip.close()
            audio_clip.close()
            os.remove(temp_video)
            os.remove(temp_html_path)
            os.remove(audio_file)
            
            print(f"Final video saved as {output_file}")
            return output_file
            
        finally:
            driver.quit()
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    

# List of major agricultural hubs in India
cities = [
    "Nashik", "Lucknow", "Vashi", "Bhubaneswar", "Chandigarh", "Patna", "Coimbatore",
    "Kochi", "Hyderabad", "Agra", "Nagpur", "Lucknow", "Jaipur", "Ahmedabad", "Delhi"
]

# List of prominent Indian languages
languages = [
    "hi", "en"
]
    

def main():
    st.title("Weather Video with Voice Narration")

    # City and Language selection
    city = st.selectbox("Select a city", cities)
    lang = st.selectbox("Select a language", languages)

    if st.button("Generate Weather Video"):
        st.write(f"Generating weather video for {city} in {lang}...")

        output_file = create_weather_video(city, lang)
        if output_file:
            st.success(f"Successfully created weather video: {output_file}")
            st.video(output_file)
            st.download_button(
                "Downloaded generated video",
                open(output_file, "rb").read(),
                f"{city}_weather.mp4",
                "video/mp4",
            )
        else:
            st.error("Failed to create weather video")

if __name__ == "__main__":
    main()