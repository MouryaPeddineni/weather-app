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
    AudioFileClip, concatenate_videoclips, TextClip, ImageClip
)
from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import translate_v2 as translate
import requests
from pydub import AudioSegment
import folium
from selenium import webdriver
from io import BytesIO


MAPS_DIR = "maps"  
VIDS_DIR = "videos"


os.makedirs(MAPS_DIR, exist_ok=True)
os.makedirs(VIDS_DIR, exist_ok=True)


# Set Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nc25572_mourya/Downloads/ttsaudio-449211-16297ceac279.json"
translator_client = translate.Client()


# API Keys (Replace with your own)
GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
# WEATHER_API_KEY = "b42f479fe23c42a591d172907251202"
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
    print(places)
    return places


def search_image(query):
    """Fetch an image using Google Custom Search API, avoiding googleusercontent.com."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": f"{query}",
        "cx": GOOGLE_CSE_ID,
        "key": GOOGLE_API_KEY,
        "searchType": "image",
        "num": 5,  # Fetch multiple images to find a valid one
    }
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "items" in data:
            for item in data["items"]:
                image_url = item["link"]
                # Filter out images from googleusercontent.com
                if "googleusercontent.com" or "maps.wikimedia.com" not in image_url:
                    return image_url  # Return first valid image
        return None  # No suitable image found
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching image: {e}")
        return None


# Initialize Google Gemini Chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, api_key=GEMINI_API_KEY)


LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "ka",
}


STATES = {
    "Andhra Pradesh": [
        {"location": "Vijayawada", "latitude": 16.5062, "longitude": 80.6480},
        {"location": "Kakinada", "latitude": 16.9891, "longitude": 82.2475},
        {"location": "Tirupati", "latitude": 13.6288, "longitude": 79.4192},
        {"location": "Visakhapatnam", "latitude": 17.6868, "longitude": 83.2185},
        {"location": "Guntur", "latitude": 16.3067, "longitude": 80.4365}
    ],
    "Telangana": [
        {"location": "Hyderabad", "latitude": 17.3850, "longitude": 78.4867},
        {"location": "Warangal", "latitude": 17.9784, "longitude": 79.5910},
        {"location": "Khammam", "latitude": 17.2473, "longitude": 80.1514},
        {"location": "Karimnagar", "latitude": 18.4386, "longitude": 79.1288}
    ],
    "Karnataka": [
        {"location": "Bengaluru", "latitude": 12.9716, "longitude": 77.5946},
        {"location": "Halasuru", "latitude": 12.9784, "longitude": 77.6224},
        {"location": "Chikkabalapur", "latitude": 13.4351, "longitude": 77.7315},
        {"location": "Mangalore", "latitude": 12.9141, "longitude": 74.8560}
    ],
    "Tamil Nadu": [
        {"location": "Chennai", "latitude": 13.0827, "longitude": 80.2707},
        {"location": "Coimbatore", "latitude": 11.0168, "longitude": 76.9558},
        {"location": "Madurai", "latitude": 9.9252, "longitude": 78.1198},
        {"location": "Tiruchirappalli", "latitude": 10.7905, "longitude": 78.7047},
        {"location": "Salem", "latitude": 11.6643, "longitude": 78.1460}
    ]
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


def save_map_as_image(city, lat, lon, temp, condition, lang):
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
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": "https://www.google.com/",  # Some sites require a referer
            }


            img_response = requests.get(img_url, headers=headers)
            img_response.raise_for_status()
            place_image = Image.open(BytesIO(img_response.content))
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Failed to fetch image: {e}")

    if place_image is None:
        place_image = Image.new("RGB", (100, 150), color=(200, 200, 200))  # Grey placeholder

    # Resize and shape the place image
    overlay_size = (int(map_image.width * 0.25), int(map_image.height * 0.40))
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

    if lang == "te":
        font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Telugu font path
    elif lang == "hi":
        font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf"  # Hindi font path
    elif lang == "kn":
        font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Kannada/NotoSansKannada-VariableFont_wdth,wght.ttf"  # Kannada font path
    elif lang == "ml":
        font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Malayalam/NotoSansMalayalam-VariableFont_wdth,wght.ttf"  # Malayalam font path
    elif lang == "ta":
        font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Tamil/NotoSansTamil-VariableFont_wdth,wght.ttf"  # Tamil font path
    else:
        font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Default font path (e.g., for English)

    try:
        font = ImageFont.truetype(font_path, 50)
    except IOError:
        font = ImageFont.load_default()

    translated_condition_label = translate_text_google("Condition", lang)
    translated_temp_label = translate_text_google("Temp", lang)

    # Define position for weather details (right side of the map)
    text_x = map_image.width - 700  # Adjust position to fit within the map
    text_y = map_image.height - 500  # Start position for text
    

    # Add semi-transparent background for readability
    overlay = Image.new("RGBA", (700, 400), (255, 255, 255, 180))  # White with transparency
    final_image.paste(overlay, (text_x - 100, text_y - 80), overlay)

    h, w = overlay.height, overlay.width
    # Overlay the weather details text
    # draw.text((text_x, text_y), "🌍 City: Example City", font=font, fill="black")

    draw.text((text_x + 20, text_y + 40), f"> {translated_temp_label}: {temp}", font=font, fill="black")
    draw.text((text_x + 20, text_y + 120), f"> {translated_condition_label} : {translate_text_google(condition, lang)}", font=font, fill="black")

    # Save the final image
    final_image_path = os.path.join(MAPS_DIR, f"{city}_map_final.jpg")
    final_image.save(final_image_path, "JPEG")

    print(f"✅ Final map with weather overlay saved: {final_image_path}")
    return final_image_path


def resize_image(image_path, target_size=(1280, 720)):
    """Resizes an image to fit the target size."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize(target_size, Image.Resampling.LANCZOS)
    output_path = f"resized_{os.path.basename(image_path)}"
    img.save(output_path)
    return output_path


def get_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 16:
        return "Good afternoon"
    else:
        return "Good evening"


def translate_text_google(text, target_lang):
    """Translates text using Google Cloud Translation API."""
    if target_lang == "en":  # No translation needed
        return text
    try:
        result = translator_client.translate(text, target_language=target_lang)
        return result["translatedText"]
    except Exception as e:
        print(f"⚠️ Google Translation failed: {e}")
        return text  # Return original text on failure


def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
    # Get the greeting (only for the first city)
    greeting = get_greeting() if is_first_city else ""

    # Translate city name
    translated_city = translate_text_google(city, lang)

    print(lang)

    hour = datetime.datetime.now().hour
    
    # Context for the AI model
    # prompt = f"""
    # You are a weather assistant. Given a city's name and weather condition, generate a beautiful and natural-sounding weather update.  

    # Generate the advice dynamically based on the conditions.

    # Keep it short, friendly, and engaging and Generate the response in the language {lang}. Do not change the language. Give the
    # response in just the desired language {lang}. Do not mix telugu or other regional languages with others
    
    # City: {city}  
    # Temperature: {temp}°C  
    # Condition: {condition}
    # """
    prompt = f"""
    You are a friendly weather advisor. Your task is to generate a *short, actionable* suggestion based on the existing weather report.  
    Phrase your suggestion in a varied and engaging manner to avoid repetitive or boring responses. Do not use greetings or salutations in between. Consider different aspects of the weather and how they might influence your suggestion. 
    Keep the suggestion to the point and give the suggestion based on the condition of the weather and time.  Try to use different phrasing each time and make the response lively.
    Before providing your suggestion, give the current weather details along with the temperature of the reporting city in a casual manner.
    Use ONLY the provided information and do not generate suggestions unrelated to the weather.  The suggestion should be specific to the given city and for the current time and weather.
    Existing Weather Suggestion: {condition} City: {city} Temperature: {temp} Time of Weather Report Generation: {hour}. Do not skip these at any cost.
    Provide your friendly suggestion below.
    """

    # Generate the weather report using the Gemini model
    response = chat_model.predict(prompt).strip()
    response = response.replace("*", "")  # Remove unwanted formatting

    print(f"🔹 AI-generated weather report for {city}: {response}")  # Debugging output

    # Translate AI-generated response (if needed)
    translated_response = translate_text_google(response, lang)

    print(f"🔹 Translated response: {translated_response}")  # Debugging output


    display_text = f"{translated_city}: {translated_response}".strip()
    audio_text = f"{translate_text_google(greeting, lang)} {translated_response}".strip()

    return display_text, audio_text


def generate_audio(text, city_name, lang="en", speed_factor=1.2):
    try:
        # Generate speech in the desired language
        temp_audio_path = f"temp_{city_name}.mp3"
        output_audio_path = f"weather_advice_{city_name}.mp3"

        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(temp_audio_path)

        # Modify speed using pydub
        audio = AudioSegment.from_mp3(temp_audio_path)
        new_audio = audio.speedup(playback_speed=speed_factor)

        # Export the final version
        new_audio.export(output_audio_path, format="mp3")

        # Remove the temporary file
        os.remove(temp_audio_path)

        return output_audio_path
    except Exception as e:
        print(f"⚠️ Audio generation failed, using fallback English: {e}")
        return None


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
 

def generate_weather_video(city_data, lang="en", output_path="/Users/nc25572_mourya/Desktop/untitled folder/output.mp4"):
    """Processes city weather data and generates a weather report video."""
    image_paths = []
    audio_paths = []

    is_first_city = True

    for _, row in city_data.iterrows():
        city_name = row['location']
        lat, lon = row['latitude'], row['longitude']

        temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
        if temp is None or condition is None:
            continue

        display_text, audio_text = generate_weather_advice(city_name, temp, condition, lang, is_first_city)
        is_first_city = False

        audio_text = f"{audio_text}"

        # Generate the map image with a popular place
        map_image_path = save_map_as_image(city_name, lat, lon, temp, condition, lang)
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

    selected_state = st.selectbox("Select State", ["None"] + list(STATES.keys()))

    if st.button("Weather report for selected state"):
        if selected_state == "None":
            st.warning("⚠️ Please select a valid state.")
        else:
            selected_state_cities = STATES[selected_state]
            print(selected_state_cities)  # Debugging
            selected_state_df = pd.DataFrame(selected_state_cities)
            
            video_path = os.path.join(VIDS_DIR, f"{selected_state}_weather_report.mp4")

            # 🔹 Step 1: Generate the video first
            generated_video_path = generate_weather_video(selected_state_df, lang=selected_lang_code, output_path=video_path)


    selected_cities = st.multiselect("Select Cities", CITY_DATA["location"])

    if st.button("Get Weather"):
        st.write("### 📍 Weather Report:")
        for city in selected_cities:
            row = CITY_DATA[CITY_DATA["location"] == city].iloc[0]
            temp, condition = fetch_weather(WEATHER_API_KEY, row["latitude"], row["longitude"])
            if temp is not None:
                weather_text = f"{city}: {temp}°C, {condition}"
                translated_text = translate_text_google(weather_text, selected_lang_code)
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