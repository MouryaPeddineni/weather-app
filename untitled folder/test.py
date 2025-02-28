# import os
# import time
# import datetime
# import requests
# import pandas as pd
# import numpy as np
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# import streamlit as st
# from moviepy.editor import (
#     ImageSequenceClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, TextClip, ImageClip
# )
# import folium
# from selenium import webdriver
# from deep_translator import GoogleTranslator
# from pydub import AudioSegment
# from langchain_google_genai import ChatGoogleGenerativeAI
# from google.cloud import translate_v2 as translate

# # Set Google credentials
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nc25572_mourya/Downloads/ttsaudio-449211-16297ceac279.json"
# translator_client = translate.Client()

# # API Keys (Replace with your own)
# WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"
# GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"

# # Initialize Google Gemini Chat model
# chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

# LANGUAGES = {
#     "English": "en",
#     "Hindi": "hi",
#     "Telugu": "te",
#     "Tamil": "ta",
#     "Kannada": "ka",
# }

# def fetch_weather(api_key, lat, lon):
#     """Fetches weather details from Weather API with retry logic."""
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
    
#     for _ in range(3):  # Retry up to 3 times
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json().get('current', {})
#             return data.get('temp_c', None), data.get('condition', {}).get('text', "")
#         time.sleep(2)
    
#     print(f"⚠️ Weather API failed for {lat}, {lon}")
#     return None, None

# def translate_text(text, target_lang="hi"):
#     """Translates text into the target language using Deep Translator."""
#     try:
#         translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)
#         return translated_text
#     except Exception as e:
#         print(f"⚠️ Translation failed: {e}")
#         return text  # Fallback to original text


# def fetch_unsplash_image(city, condition):
#     """Fetches a relevant background image from Unsplash based on weather conditions."""
#     query = f"{city}"
#     url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}&orientation=landscape"

#     response = requests.get(url)
#     if response.status_code == 200:
#         image_url = response.json().get("urls", {}).get("regular")
#         if image_url:
#             image_path = f"backgrounds/{city}.jpg"
#             os.makedirs("backgrounds", exist_ok=True)
#             img_data = requests.get(image_url).content
#             with open(image_path, "wb") as img_file:
#                 img_file.write(img_data)
#             return resize_image(image_path)

#     print(f"⚠️ Failed to fetch background for {city}, using fallback.")
#     return resize_image("fallback.jpg")  # Ensure fallback image is always available


# def create_scrolling_text(text, duration, video_size=(1280, 720), font_size=50, font_color="white"):
#     """Generates a scrolling text overlay moving from right to left."""
#     txt_clip = TextClip(text, fontsize=font_size, color=font_color, font="Arial-Bold")

#     text_width, text_height = txt_clip.size
#     start_x = video_size[0]  # Start from the right side
#     end_x = -text_width  # Move to the left until text is out of view

#     # Animate the position from right to left
#     txt_clip = txt_clip.set_position(lambda t: (start_x - (start_x - end_x) * (t / duration), video_size[1] - 100))
#     txt_clip = txt_clip.set_duration(duration)

#     return txt_clip

# def create_video(image_sequences, audio_files, weather_texts, output_file="weather_report.mp4"):
#     """Creates a weather report video with map, background, and scrolling weather data."""
#     final_clips = []

#     for images, audio_file, weather_text in zip(image_sequences, audio_files, weather_texts):
#         audio_clip = AudioFileClip(audio_file)
#         duration = audio_clip.duration  

#         # --- Create Zoom-in Effect for Map (First 2 Seconds) ---
#         zoom_frames = []
#         map_image = Image.open(images[0])  

#         for scale in np.linspace(1, 1.2, num=10):  # Gradually zoom in
#             width, height = map_image.size
#             new_width, new_height = int(width * scale), int(height * scale)
#             zoomed_img = map_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

#             left = (new_width - width) // 2
#             top = (new_height - height) // 2
#             zoomed_img = zoomed_img.crop((left, top, left + width, top + height))

#             frame_path = f"temp_zoom_{scale:.2f}.jpg"
#             zoomed_img.save(frame_path)
#             zoom_frames.append(frame_path)

#         map_clip = ImageSequenceClip(zoom_frames, fps=10).set_duration(2).crossfadeout(1)

#         # --- Background Image for Remaining Duration ---
#         background_clip = ImageClip(images[1]).set_duration(max(0.1, duration - 2)).crossfadein(1)

#         # Combine Map Zoom-in + Background
#         video_clip = concatenate_videoclips([map_clip, background_clip], method="compose")
#         video_clip = video_clip.set_audio(audio_clip)

#         # --- Add Scrolling Text Overlay (Right to Left) ---
#         scrolling_text_clip = create_scrolling_text(weather_text, duration)
#         video_with_text = CompositeVideoClip([video_clip, scrolling_text_clip])

#         final_clips.append(video_with_text)

#     # --- Merge All Clips Together ---
#     final_video = concatenate_videoclips(final_clips, method="compose")
#     final_video.write_videofile(output_file, codec="libx264", fps=30, bitrate="5000k")
#     final_video.close()



# def create_map(lat, lon, city_name):
#     """Generates a map for each city."""
#     try:
#         os.makedirs("maps", exist_ok=True)
#         map_file = f"maps/{city_name}.html"

#         folium_map = folium.Map(location=[lat, lon], zoom_start=12)
#         folium.Marker([lat, lon], popup=city_name).add_to(folium_map)
#         folium_map.save(map_file)

#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--window-size=1280x720")

#         driver = webdriver.Chrome(options=options)
#         driver.get(f"file://{os.path.abspath(map_file)}")

#         time.sleep(3)  # Allow rendering
#         screenshot_path = f"maps/{city_name}.png"
#         driver.save_screenshot(screenshot_path)
#         driver.quit()

#         return resize_image(screenshot_path)

#     except Exception as e:
#         print(f"⚠️ Failed to generate map for {city_name}, using default map.")
#         return "default_map.png"

# def resize_image(image_path, target_size=(1280, 720)):
#     """Resizes an image to fit the target size."""
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize(target_size, Image.Resampling.LANCZOS)
#     output_path = f"resized_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path

# def generate_audio(text, city_name, lang="hi"):
#     """Generates an audio file from translated text using gTTS."""
#     try:
#         translated_text = translate_text(text, lang) if lang != "en" else text
#         audio_file = f"weather_audio_{city_name}_{lang}.mp3"
#         tts = gTTS(text=translated_text, lang=lang, slow=False)
#         tts.save(audio_file)
#         return audio_file
#     except Exception as e:
#         print(f"⚠️ Audio generation failed: {e}")
#         return None


# def generate_weather_video(city_data, lang="hi"):
#     """Processes city weather data and generates a weather report video in the selected language."""
#     image_sequences = []
#     audio_paths = []
#     weather_texts = []

#     for _, row in city_data.iterrows():
#         city_name = row['location']
#         lat, lon = row['latitude'], row['longitude']

#         temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
#         if temp is None or condition is None:
#             continue

#         greeting_english = "Good morning" if datetime.datetime.now().hour < 12 else "Good evening"
#         greeting_translated = translate_text(greeting_english, lang)


#         prompt = f"{city_name}: {temp}°C, {condition}. Provide a short weather suggestion."
#         response = chat_model.predict(prompt).strip().replace("*", "")

#         audio_text = f"{greeting_translated} {city_name}, the temperature is {temp}°C with {condition}. {response}"
#         display_text = f"{city_name}: {temp}°C, {condition}."

#         map_image = create_map(lat, lon, city_name)
#         background_image = fetch_unsplash_image(city_name, condition)

#         if map_image and background_image:
#             image_sequences.append([map_image, background_image])
#             audio_path = generate_audio(audio_text, city_name, lang)
#             if audio_path:
#                 audio_paths.append(audio_path)
#             weather_texts.append(display_text)
#         else:
#             print(f"⚠️ Skipping {city_name} due to missing images.")

#     if image_sequences and audio_paths:
#         create_video(image_sequences, audio_paths, weather_texts)

# import streamlit as st
# import pandas as pd

# # File Uploader for Custom City Data
# uploaded_file = st.file_uploader("Upload CSV file (Location, Latitude, Longitude)", type=["csv"])

# # Check if the file is uploaded
# if uploaded_file:
#     CITY_DATA = pd.read_csv(uploaded_file)
#     if not {'location', 'latitude', 'longitude'}.issubset(CITY_DATA.columns):
#         st.error("❌ Uploaded file must contain 'Location', 'Latitude', and 'Longitude' columns.")
#         CITY_DATA = None  # Set to None if invalid
# else:
#     CITY_DATA = None
#     st.warning("⚠️ Please upload a CSV file containing 'Location', 'Latitude', and 'Longitude'.")

# # Proceed only if CITY_DATA is available
# if CITY_DATA is not None:
#     # Language Selection
#     selected_lang = st.selectbox("Select Language", list(LANGUAGES.keys()))
#     selected_lang_code = LANGUAGES[selected_lang]  # Get language code

#     # City Selection
#     selected_cities = st.multiselect("Select Cities", CITY_DATA["location"])

#     # Fetch Weather Button
#     if st.button("Get Weather"):
#         st.write("### 📍 Weather Report:")
#         for city in selected_cities:
#             row = CITY_DATA[CITY_DATA["location"] == city].iloc[0]
#             temp, condition = fetch_weather(WEATHER_API_KEY, row["latitude"], row["longitude"])
#             if temp is not None:
#                 weather_text = f"{city}: {temp}°C, {condition}"
#                 translated_text = translate_text(weather_text, selected_lang_code)
#                 st.success(translated_text)
#             else:
#                 st.error(f"⚠️ Could not fetch weather for {city}")

#     # Generate Weather Video Button
#     if st.button("Generate Weather Video"):
#         st.info("Generating video... (This may take some time)")
        
#         # Filter selected cities for processing
#         selected_city_data = CITY_DATA[CITY_DATA["location"].isin(selected_cities)]
        
#         if not selected_city_data.empty:
#             generate_weather_video(selected_city_data, lang=selected_lang_code)  # Pass selected_lang_code
#             st.success("✅ Video generated successfully! Download below:")

#             video_path = "weather_report.mp4"
#             with open(video_path, "rb") as file:
#                 st.download_button(
#                     label="📥 Download Weather Video",
#                     data=file,
#                     file_name="weather_report.mp4",
#                     mime="video/mp4"
#                 )

#             st.video(video_path)
#         else:
#             st.warning("⚠️ Please select at least one city before generating the video.")


# def create_marker_shape(image):
#     """Convert the fetched image into a marker shape with a larger rounded top and tapered bottom."""
#     size = image.size
#     mask = Image.new("L", size, 0)
#     draw = ImageDraw.Draw(mask)

#     # Increase the height of the rounded top
#     rounded_top_height = int(size[1] * 0.80)  # Increased from 0.70 to 0.80

#     draw.ellipse((0, 0, size[0], rounded_top_height), fill=255)  # Larger rounded top
#     draw.polygon(
#         [(size[0] // 2, size[1] * 0.95), (0, size[1] * 0.5), (size[0], size[1] * 0.5)], fill=255
#     )  # Pointed bottom

#     # Apply the mask
#     marker_image = ImageOps.fit(image, size, centering=(0.5, 0.5))
#     marker_image.putalpha(mask)

#     return marker_image


# def save_map_as_image(city, lat, lon):
#     """Generate a Folium map and save it as an image with an overlay in a map marker shape."""
#     places = get_popular_places(city)
#     if not places:
#         print(f"⚠️ No popular places found in {city}.")
#         return None

#     img_url = None
#     popular_place = None

#     for place in places:
#         img_url = search_image(place["name"])
#         if img_url:
#             popular_place = place
#             break

#     if not popular_place:
#         print("⚠️ No valid image found.")
#         return None

#     print(f"Selected Place: {popular_place['name']}")
#     print(f"Image URL: {img_url}")

#     # Create a city map image using provided latitude and longitude
#     city_map_path = create_map(lat, lon, city)

#     if not os.path.exists(city_map_path):
#         print(f"⚠️ Map image not found: {city_map_path}")
#         return None

#     # Open the city map image
#     map_image = Image.open(city_map_path)

#     # Fetch and process the place image
#     place_image = None
#     if img_url:
#         try:
#             headers = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#             }

#             img_response = requests.get(img_url, headers=headers)
#             img_response.raise_for_status()
#             place_image = Image.open(BytesIO(img_response.content))
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Failed to fetch image: {e}")

#     if place_image is None:
#         place_image = Image.new("RGB", (100, 150), color=(200, 200, 200))  # Grey placeholder

#     # Resize and shape the place image
#     overlay_size = (int(map_image.width * 0.30), int(map_image.height * 0.45))
#     place_image = place_image.resize(overlay_size)
#     place_image = create_marker_shape(place_image)

#     # Add city name in bold to the top-left of place_image
#     draw = ImageDraw.Draw(place_image)

#     place_image_cv = np.array(place_image)
#     place_image_cv = cv2.cvtColor(place_image_cv, cv2.COLOR_RGB2BGR)

#     # Define text properties
#     text = city
#     font_size = 40  # Adjust as needed
#     font_color = "white"
#     stroke_color = "black"
#     stroke_width = 3  # Outline thickness

#     # Create text clip
#     text_clip = TextClip(text, fontsize=font_size, color=font_color, stroke_color=stroke_color, stroke_width=stroke_width, font="Arial-Bold")

#     # Convert text clip to an image array
#     text_array = text_clip.get_frame(0)

#     # Convert RGBA to BGR (remove alpha channel)
#     text_array = cv2.cvtColor(text_array, cv2.COLOR_RGBA2BGR)  # Drop alpha

#     # Get text dimensions
#     text_height, text_width = text_array.shape[:2]

#     # Define text position (top-left of place_image)
#     text_x, text_y = 10, 10

#     # Ensure the text fits within the image bounds
#     if text_y + text_height > place_image_cv.shape[0] or text_x + text_width > place_image_cv.shape[1]:
#         raise ValueError("Text exceeds image boundaries!")

#     # Overlay text onto the image
#     overlay = place_image_cv.copy()
#     overlay[text_y:text_y + text_height, text_x:text_x + text_width] = text_array  # No alpha issue now

#     # Convert back to PIL image
#     place_image = Image.fromarray(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))


#     # try:
#     #     font = ImageFont.truetype("arial.ttf", 30)  # Adjust font size as needed
#     #     print(font)
#     # except IOError:
#     #     font = ImageFont.load_default()

#     # text_position = (10, 10)  # Top-left position
#     # text_color = (255, 255, 255)  # White color for contrast
#     # outline_color = (0, 0, 0)  # Black outline for readability

#     # # Add outline for better visibility
#     # for dx in [-1, 1]:
#     #     for dy in [-1, 1]:
#     #         draw.text((text_position[0] + dx, text_position[1] + dy), city, font=font, fill=outline_color)

#     # draw.text(text_position, city, font=font, fill=text_color)

#     # Approximate marker position
#     marker_x = map_image.width // 2
#     marker_y = map_image.height // 2

#     # Place the overlay just above the marker
#     position = (marker_x - overlay_size[0] // 2, marker_y - overlay_size[1] - 10)

#     map_image.paste(place_image, position, place_image)

#     # Save the final image
#     final_image_path = os.path.join(MAPS_DIR, f"{city}_map_final.jpg")
#     map_image.convert("RGB").save(final_image_path, "JPEG")

#     print(f"✅ Final map with marker-shaped overlay saved: {final_image_path}")
#     return final_image_path


# import cv2
# import numpy as np
# from PIL import Image, ImageDraw

# def save_map_as_image(city, lat, lon):
#     """Generate a Folium map and save it as an image with an overlay in a map marker shape."""
#     places = get_popular_places(city)
#     if not places:
#         print(f"⚠️ No popular places found in {city}.")
#         return None

#     img_url = None
#     popular_place = None

#     for place in places:
#         img_url = search_image(place["name"])
#         if img_url:
#             popular_place = place
#             break

#     if not popular_place:
#         print("⚠️ No valid image found.")
#         return None

#     print(f"Selected Place: {popular_place['name']}")
#     print(f"Image URL: {img_url}")

#     # Create a city map image using provided latitude and longitude
#     city_map_path = create_map(lat, lon, city)

#     if not os.path.exists(city_map_path):
#         print(f"⚠️ Map image not found: {city_map_path}")
#         return None

#     # Open the city map image
#     map_image = Image.open(city_map_path)

#     # Fetch and process the place image
#     place_image = None
#     if img_url:
#         try:
#             headers = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#             }

#             img_response = requests.get(img_url, headers=headers)
#             img_response.raise_for_status()
#             place_image = Image.open(BytesIO(img_response.content))
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Failed to fetch image: {e}")

#     if place_image is None:
#         place_image = Image.new("RGB", (100, 150), color=(200, 200, 200))  # Grey placeholder

#     # Resize and shape the place image
#     overlay_size = (int(map_image.width * 0.30), int(map_image.height * 0.45))
#     place_image = place_image.resize(overlay_size)
#     place_image = create_marker_shape(place_image)

#     # Convert place image to OpenCV format
#     place_image_cv = np.array(place_image)
#     place_image_cv = cv2.cvtColor(place_image_cv, cv2.COLOR_RGB2BGR)

#     # Define text properties
#     text = city
#     font_scale = 1.5  # Adjust based on image size
#     font_thickness = 3
#     font = cv2.FONT_HERSHEY_SIMPLEX

#     # Get text size
#     text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
#     text_x, text_y = 20, text_size[1] + 10  # Position at top-left with padding

#     # Ensure text fits within the image bounds
#     text_x = max(10, text_x)
#     text_y = min(place_image_cv.shape[0] - 10, text_y)

#     # Draw text with outline
#     cv2.putText(place_image_cv, text, (text_x + 1, text_y + 1), font, font_scale, (0, 0, 0), font_thickness + 2, cv2.LINE_AA)  # Black outline
#     cv2.putText(place_image_cv, text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)  # White text

#     # Convert back to PIL image
#     place_image = Image.fromarray(cv2.cvtColor(place_image_cv, cv2.COLOR_BGR2RGB))

#     # Approximate marker position
#     marker_x = map_image.width // 2
#     marker_y = map_image.height // 2

#     # Place the overlay just above the marker
#     position = (marker_x - overlay_size[0] // 2, marker_y - overlay_size[1] - 10)

#     map_image.paste(place_image, position, place_image)

#     # Save the final image
#     final_image_path = os.path.join(MAPS_DIR, f"{city}_map_final.jpg")
#     map_image.convert("RGB").save(final_image_path, "JPEG")

#     print(f"✅ Final map with marker-shaped overlay saved: {final_image_path}")
#     return final_image_path



import os
import time
import datetime
import requests
import pandas as pd
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import streamlit as st
from moviepy.editor import (
    ImageSequenceClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, TextClip, ImageClip
)
from deep_translator import GoogleTranslator
from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import translate_v2 as translate
import requests
import folium
import os
import time
from selenium import webdriver
from io import BytesIO
import numpy as np
import cv2

MAPS_DIR = "maps"  # Ensure this directory exists

MAPS_DIR = "maps"
os.makedirs(MAPS_DIR, exist_ok=True)

# Set Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nc25572_mourya/Downloads/ttsaudio-449211-16297ceac279.json"
translator_client = translate.Client()

# API Keys (Replace with your own)
GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
GOOGLE_CSE_ID = "3269dbbc6cdf0482b"
GOOGLE_PLACES_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"



def get_popular_places(city):
    """Fetch popular tourist attractions in a city using Google Places API."""
    query = f"tourist attractions in {city}"
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
    return places


def search_image(query):
    """Fetch an image using Google Custom Search API."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "cx": GOOGLE_CSE_ID,
        "key": GOOGLE_API_KEY,
        "searchType": "image",
        "num": 1,
    }
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "items" in data:
            for item in data["items"]:
                image_url = item["link"]
                return image_url  # Return first image
        return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching image: {e}")
        return None


# Initialize Google Gemini Chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "ka",
}

def fetch_weather(api_key, lat, lon):
    """Fetches weather details from Weather API with retry logic."""
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
    
    for _ in range(3):  # Retry up to 3 times
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get('current', {})
            return data.get('temp_c', None), data.get('condition', {}).get('text', "")
        time.sleep(2)
    
    print(f"⚠️ Weather API failed for {lat}, {lon}")
    return None, None

def translate_text(text, target_lang="hi"):
    """Translates text into the target language using Deep Translator."""
    try:
        translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)
        return translated_text
    except Exception as e:
        print(f"⚠️ Translation failed: {e}")
        return text  # Fallback to original text
    


def create_map(lat, lon, city_name):
    """Generate a map and capture a screenshot as an image."""
    map_file = f"maps/{city_name}.html"
    folium_map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker(
        [lat - 0.015, lon], popup=city_name, icon=folium.Icon(icon="cloud", color="blue")
    ).add_to(folium_map)

    folium_map.save(map_file)

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=800x600")

    driver = webdriver.Chrome(options=options)
    driver.get(f"file://{os.path.abspath(map_file)}")
    time.sleep(2)

    # Save the screenshot
    screenshot_path = f"maps/{city_name}.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    # Convert PNG to JPG
    img = Image.open(screenshot_path)
    jpg_path = f"maps/{city_name}_img.jpg"
    img.convert("RGB").save(jpg_path, "JPEG")
    os.remove(screenshot_path)

    print(f"✅ Map saved as {jpg_path}")
    return jpg_path


def save_map_as_image(city, lat, lon, temp, condition):
    """Generate a Folium map and save it as an image with an overlay in a map marker shape."""
    places = get_popular_places(city)
    if not places:
        print(f"⚠️ No popular places found in {city}.")
        return None

    img_url = None
    popular_place = None

    for place in places:
        img_url = search_image(place["name"])
        if img_url:
            popular_place = place
            break

    if not popular_place:
        print("⚠️ No valid image found.")
        return None

    print(f"Selected Place: {popular_place['name']}")
    print(f"Image URL: {img_url}")

    # Create a city map image using provided latitude and longitude
    city_map_path = create_map(lat, lon, city)

    if not os.path.exists(city_map_path):
        print(f"⚠️ Map image not found: {city_map_path}")
        return None

    # Open the city map image
    map_image = Image.open(city_map_path)

    # Fetch and process the place image
    place_image = None
    if img_url:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            img_response = requests.get(img_url, headers=headers)
            img_response.raise_for_status()
            place_image = Image.open(BytesIO(img_response.content))
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Failed to fetch image: {e}")

    if place_image is None:
        place_image = Image.new("RGB", (100, 150), color=(200, 200, 200))  # Grey placeholder

    # Resize and shape the place image
    overlay_size = (int(map_image.width * 0.30), int(map_image.height * 0.45))
    place_image = place_image.resize(overlay_size)
    # place_image = create_marker_shape(place_image)

    # Convert place_image to OpenCV format (BGR)
    place_image_cv = np.array(place_image)
    place_image_cv = cv2.cvtColor(place_image_cv, cv2.COLOR_RGB2BGR)

    # Define text properties
    text = city
    font_size = 40  # Adjust as needed
    font_color = "white"
    stroke_color = "black"
    stroke_width = 3  # Outline thickness

    # Create text clip using MoviePy
    text_clip = TextClip(
        text, fontsize=font_size, color=font_color, 
        stroke_color=stroke_color, stroke_width=stroke_width, font="Arial-Bold"
    )

    # Convert text clip to an image array (RGBA)
    # Convert text clip to an image array (ensure it's RGBA)
    text_array = text_clip.get_frame(0)  # Shape should be (H, W, 4)

    # Ensure text_array has an alpha channel
    if text_array.shape[-1] == 3:  # If it's RGB, add an alpha channel
        alpha_channel = np.full((text_array.shape[0], text_array.shape[1]), 255, dtype=np.uint8)
        text_array = np.dstack([text_array, alpha_channel])  # Convert to RGBA

    # Split into color and alpha channels
    text_rgb = text_array[:, :, :3]  # RGB channels
    text_alpha = text_array[:, :, 3] / 255.0  # Normalize alpha channel


    # Get text dimensions
    text_height, text_width = text_rgb.shape[:2]

    # Define text position (top-left of place_image)
    text_x, text_y = 80, 80

    # Ensure overlay shape matches the base image (handles transparency correctly)
    overlay = place_image_cv.copy()

    # Blend the text into the place image using alpha blending
    for c in range(3):  # Apply blending for R, G, B channels
        overlay[text_y:text_y + text_height, text_x:text_x + text_width, c] = (
            (1 - text_alpha) * overlay[text_y:text_y + text_height, text_x:text_x + text_width, c] +
            text_alpha * text_rgb[:, :, c]
        ).astype(np.uint8)

    # Convert back to PIL image
    place_image = Image.fromarray(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))
    # place_image = create_marker_shape(place_image)

    # Approximate marker position
    marker_x = map_image.width // 2
    marker_y = map_image.height // 2

    # Place the overlay just above the marker
    position = (marker_x - overlay_size[0] // 2, marker_y - overlay_size[1] - 10)

    # Convert place_image to RGBA before pasting
    place_image = place_image.convert("RGBA")

    # Create a new RGBA background (same size as map_image)
    background = Image.new("RGBA", map_image.size, (255, 255, 255, 255))

    # Paste the map image first
    background.paste(map_image.convert("RGBA"), (0, 0))

    # Paste the place_image with proper transparency handling
    background.paste(place_image, position, place_image)

    text_x = map_image.width + 20  # Position text on the right side
    text_y = 50

    # Keep the original map image size
    final_image = background.convert("RGB")
    draw = ImageDraw.Draw(final_image)

    # Load a font (adjust path if necessary)
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    try:
        font = ImageFont.truetype(font_path, 50)
    except IOError:
        font = ImageFont.load_default()

    # Define position for weather details (right side of the map)
    text_x = map_image.width - 600  # Adjust position to fit within the map
    text_y = map_image.height - 400  # Start position for text

    # Hardcoded weather details
    # hardcoded_temp = "28°C"
    # hardcoded_condition = "Partly Cloudy"

    # Add semi-transparent background for readability
    overlay = Image.new("RGBA", (500, 300), (255, 255, 255, 180))  # White with transparency
    final_image.paste(overlay, (text_x - 20, text_y - 10), overlay)

    # Overlay the weather details text
    # draw.text((text_x, text_y), "🌍 City: Example City", font=font, fill="black")
    draw.text((text_x + 20, text_y + 40), f"Temp: {temp}", font=font, fill="black")
    draw.text((text_x + 20, text_y + 120), f"Condition: {condition}", font=font, fill="black")

    # Save the final image
    final_image_path = os.path.join(MAPS_DIR, f"{city}_map_final.jpg")
    final_image.save(final_image_path, "JPEG")

    print(f"✅ Final map with weather overlay saved: {final_image_path}")
    return final_image_path



from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def create_video(image_paths, audio_files, output_file="weather_report.mp4"):
    """Creates a weather report video with only generated maps and audio."""
    final_clips = []

    for img_path, audio_path in zip(image_paths, audio_files):
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration  

        # Create image clip with same duration as audio
        image_clip = ImageClip(img_path).set_duration(duration).set_audio(audio_clip)

        final_clips.append(image_clip)

    # Concatenate all clips
    final_video = concatenate_videoclips(final_clips, method="compose")
    final_video.write_videofile(output_file, codec="libx264", fps=24, bitrate="2000k")
    final_video.close()



# def create_scrolling_text(text, duration, video_size=(1280, 720), font_size=50, font_color="white"):
#     """Generates a scrolling text overlay moving from right to left."""
#     txt_clip = TextClip(text, fontsize=font_size, color=font_color, font="Arial-Bold")

#     text_width, text_height = txt_clip.size
#     start_x = video_size[0]  # Start from the right side
#     end_x = -text_width  # Move to the left until text is out of view

#     # Animate the position from right to left
#     txt_clip = txt_clip.set_position(lambda t: (start_x - (start_x - end_x) * (t / duration), video_size[1] - 100))
#     txt_clip = txt_clip.set_duration(duration)

#     return txt_clip


def resize_image(image_path, target_size=(1280, 720)):
    """Resizes an image to fit the target size."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize(target_size, Image.Resampling.LANCZOS)
    output_path = f"resized_{os.path.basename(image_path)}"
    img.save(output_path)
    return output_path


def generate_audio(text, city_name, lang="hi"):
    """Generates an audio file from translated text using gTTS."""
    try:
        translated_text = translate_text(text, lang) if lang != "en" else text
        audio_file = f"weather_audio_{city_name}_{lang}.mp3"
        tts = gTTS(text=translated_text, lang=lang, slow=False)
        tts.save(audio_file)
        return audio_file
    except Exception as e:
        print(f"⚠️ Audio generation failed: {e}")
        return None
    

def generate_weather_video(city_data, lang="hi"):
    """Processes city weather data and generates a weather report video."""
    image_paths = []
    audio_paths = []

    for _, row in city_data.iterrows():
        city_name = row['location']
        lat, lon = row['latitude'], row['longitude']

        temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
        if temp is None or condition is None:
            continue

        hr = datetime.datetime.now().hour
        if hr < 12:
            greeting_english = "Good morning"
        elif hr < 16:  # Till 4 PM
            greeting_english = "Good Afternoon"
        else:
            greeting_english = "Good Evening"

        greeting_translated = translate_text(greeting_english, lang)

        prompt = f"{city_name}: {temp}°C, {condition}. Provide a short weather suggestion."
        response = chat_model.predict(prompt).strip().replace("*", "")

        audio_text = f"{greeting_translated} {response}"

        # Generate the map image with a popular place
        map_image_path = save_map_as_image(city_name, lat, lon, temp, condition)
        if map_image_path:
            image_paths.append(map_image_path)

        # Generate the audio file
        audio_path = generate_audio(audio_text, city_name, lang)
        if audio_path:
            audio_paths.append(audio_path)

    if image_paths and audio_paths:
        create_video(image_paths, audio_paths)




# Streamlit UI
st.title("🌤️ Weather Report Video Generator")

uploaded_file = st.file_uploader("Upload CSV file (Location, Latitude, Longitude)", type=["csv"])

if uploaded_file:
    CITY_DATA = pd.read_csv(uploaded_file)
    if not {'location', 'latitude', 'longitude'}.issubset(CITY_DATA.columns):
        st.error("❌ Uploaded file must contain 'Location', 'Latitude', and 'Longitude' columns.")
        CITY_DATA = None
else:
    CITY_DATA = None
    st.warning("⚠️ Please upload a CSV file containing 'Location', 'Latitude', and 'Longitude'.")

if CITY_DATA is not None:
    selected_lang = st.selectbox("Select Language", list(LANGUAGES.keys()))
    selected_lang_code = LANGUAGES[selected_lang]  

    selected_cities = st.multiselect("Select Cities", CITY_DATA["location"])

    if st.button("Get Weather"):
        st.write("### 📍 Weather Report:")
        for city in selected_cities:
            row = CITY_DATA[CITY_DATA["location"] == city].iloc[0]
            temp, condition = fetch_weather(WEATHER_API_KEY, row["latitude"], row["longitude"])
            if temp is not None:
                weather_text = f"{city}: {temp}°C, {condition}"
                translated_text = translate_text(weather_text, selected_lang_code)
                st.success(translated_text)
            else:
                st.error(f"⚠️ Could not fetch weather for {city}")

    if st.button("Generate Weather Video"):
        st.info("Generating video... (This may take some time)")
        
        selected_city_data = CITY_DATA[CITY_DATA["location"].isin(selected_cities)]
        
        if not selected_city_data.empty:
            generate_weather_video(selected_city_data, lang=selected_lang_code)
            st.success("✅ Video generated successfully! Download below:")

            video_path = "weather_report.mp4"
            with open(video_path, "rb") as file:
                st.download_button("📥 Download Weather Video", file, "weather_report.mp4", "video/mp4")
            st.video(video_path)
        else:
            st.warning("⚠️ Please select at least one city before generating the video.")