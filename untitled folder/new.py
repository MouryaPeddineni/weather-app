# import os
# import time
# import datetime
# import requests
# import pandas as pd
# import numpy as np
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import (
#     ImageSequenceClip, AudioFileClip, concatenate_videoclips
# )
# import folium
# from selenium import webdriver
# from deep_translator import GoogleTranslator
# from pydub import AudioSegment
# from langchain_google_genai import ChatGoogleGenerativeAI  # Google Gemini AI
# from google.cloud import translate_v2 as translate
# import os


# # Set Google credentials
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nc25572_mourya/Downloads/ttsaudio-449211-16297ceac279.json"

# translator_client = translate.Client()


# # API Keys (Replace with your own)
# WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"
# GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"

# # Initialize Google Gemini Chat model
# chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

# # Get time-based greeting
# def get_greeting():
#     hour = datetime.datetime.now().hour
#     return "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"

# # Fetch weather details
# def fetch_weather(api_key, lat, lon):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
#     response = requests.get(url)
#     # print(response.json())
#     for _ in range(3):  # Retry up to 3 times
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()['current']['temp_c'], response.json()['current']['condition']['text']
#         time.sleep(2)  # Wait before retrying
#     # print(f"⚠️ Weather API failed for {lat}, {lon} with status: {response.status_code}")
#     return None, None


# def translate_text_google(text, target_lang):
#     """Translates text using Google Cloud Translation API."""
#     if target_lang == "en":  # No translation needed
#         return text
#     try:
#         result = translator_client.translate(text, target_language=target_lang)
#         return result["translatedText"]
#     except Exception as e:
#         print(f"⚠️ Google Translation failed: {e}")
#         return text  # Return original text on failure


# # Generate AI-based weather advice
# from deep_translator import GoogleTranslator


# def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
#     # Get the greeting (only for the first city)
#     greeting = get_greeting() if is_first_city else ""

#     # Translate city name
#     translated_city = translate_text_google(city, lang)
    
#     # Translate weather condition
#     translated_condition = translate_text_google(condition, lang)

#     # Translate temperature phrase
#     translated_temp = translate_text_google(f"The temperature is {temp}°C.", lang)

#     # AI-based weather suggestion
#     context = f"{city}: {temp}°C, {condition}."
#     prompt = f"""{context} 
#     Give a very short and clear weather suggestion in one sentence. 
#     Example: "Carry an umbrella if it rains." or "Wear warm clothes if it's cold."
#     Do NOT include labels like "Suggestion:" in the response."""

#     response = chat_model.predict(prompt).strip()
#     response = response.replace("*", "")  # Remove unwanted formatting

#     print(f"Generated Suggestion for {city}: {response}")  # Debugging output

#     # Translate the suggestion
#     translated_suggestion = translate_text_google(response, lang)

#     # Final text for the audio (includes weather details and suggestion)
#     audio_text = f"{greeting} {translated_city}, {translated_temp}, {translated_condition}. {translated_suggestion}".strip()

#     # Final text for display (weather report text)
#     display_text = f"{translated_city}: {temp}°C, {translated_condition}. {translated_suggestion}".strip()

#     return display_text, audio_text




# # Download background image from Unsplash
# def download_background_image(city, weather_condition, save_path="backgrounds"):
#     os.makedirs(save_path, exist_ok=True)
    
#     query = f"{weather_condition} weather scenery"
#     url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         image_url = data["urls"].get("full")
#         if image_url:
#             image_path = os.path.join(save_path, f"{city}_{weather_condition}.jpg")
#             img_data = requests.get(image_url).content
#             with open(image_path, "wb") as img_file:
#                 img_file.write(img_data)

#             # Resize the image to fit 1280x720 without cropping
#             resized_image_path = resize_image(image_path, (1280, 720))
#             return resized_image_path

#     return "fallback.jpg"  # Use a fallback image if API fails


# def resize_image(image_path, target_size=(1280, 720)):
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize(target_size, Image.Resampling.LANCZOS)  # Resize exactly to target size

#     output_path = f"resized_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path



# def resize_map_image(map_path, target_size=(1280, 720)):
#     img = Image.open(map_path).convert("RGB")
#     img = img.resize(target_size, Image.Resampling.LANCZOS)

#     output_path = f"resized_{os.path.basename(map_path)}"
#     img.save(output_path)
#     return output_path


# # Generate a map image with a marker
# def create_map(lat, lon, city_name):
#     os.makedirs("maps", exist_ok=True)
#     map_file = f"maps/{city_name}.html"
    
#     folium_map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(folium_map)
#     folium_map.save(map_file)

#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)
    
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     return screenshot_path

# # Add text overlay to an image
# def add_text_overlay(image_path, text):
#     img = Image.open(image_path).convert("RGB")
#     target_size = (1280, 720)
#     img = img.resize(target_size, Image.Resampling.LANCZOS)  # Maintain uniform size

#     draw = ImageDraw.Draw(img)

#     try:
#         font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"  # Update if needed
#         font = ImageFont.truetype(font_path, 50)
#     except OSError:
#         print("⚠️ Font file not found, using default font.")
#         font = ImageFont.load_default()

#     text_position = (50, 50)
#     draw.text(text_position, text, fill="white", font=font)

#     output_path = f"overlay_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path



# # Generate audio from text for each city
# def generate_audio(text, city_name, lang="en"):
#     try:
#         # Generate speech in the desired language
#         audio_file = f"weather_advice_{city_name}.mp3"
#         tts = gTTS(text=text, lang=lang, slow=False)
#         tts.save(audio_file)
#         return audio_file
#     except Exception as e:
#         print(f"⚠️ Audio generation failed, using fallback English: {e}")
#         return None  # Return None if audio generation fails


# # Merge all audio files into a single file
# def merge_audio(audio_files, output_file="final_weather_audio.mp3"):
#     combined = AudioSegment.empty()
    
#     for audio_file in audio_files:
#         sound = AudioSegment.from_file(audio_file, format="mp3")
#         combined += sound + AudioSegment.silent(duration=500)  # Add 0.5 sec silence between clips

#     combined.export(output_file, format="mp3")
#     return output_file

# # Create video sequence
# # Create video sequence with separate audio clips for each city
# def create_video(image_sequences, audio_files, output_file="weather_report.mp4"):
#     final_clips = []

#     for images, audio_file in zip(image_sequences, audio_files):  # Use each city's audio separately
#         audio_clip = AudioFileClip(audio_file)
#         duration = audio_clip.duration

#         # Show map image for 2 seconds
#         map_clip = ImageSequenceClip([images[0]], durations=[2])

#         # Show background image for the remaining time
#         background_clip = ImageSequenceClip([images[1]], durations=[duration - 2])

#         # Crossfade transition
#         video_clip = concatenate_videoclips([map_clip, background_clip], method="compose").crossfadein(1)
#         video_clip = video_clip.set_audio(audio_clip)  # Attach the corresponding audio clip
        
#         final_clips.append(video_clip)

#     final_video = concatenate_videoclips(final_clips)
#     final_video.write_videofile(output_file, codec="libx264", fps=30, bitrate="5000k", preset="medium")
#     final_video.close()



# # Main function to process cities and generate weather video
# # Main function to process cities and generate weather video
# def generate_weather_video(city_data):
#     image_sequences = []
#     audio_paths = []

#     for index, row in city_data.iterrows():
#         city_name = row['Location']
#         lat, lon = row['Latitude'], row['Longitude']

#         temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
#         # print(temp, condition)
#         display_text, audio_text = generate_weather_advice(city_name, temp, condition, lang="te", is_first_city=(index == 0))

#         # Download background image
#         background_image = resize_image(download_background_image(city_name, condition))
#         background_image = add_text_overlay(background_image, display_text)


#         map_image = resize_map_image(create_map(lat, lon, city_name))  # Ensure same size

#         # Prepare image sequence
#         image_sequences.append([map_image, background_image])


#         # Generate separate audio file for each city
#         audio_path = generate_audio(audio_text, city_name, lang="te")

#         audio_paths.append(audio_path)

#     # Generate final video (Pass separate audio clips)
#     create_video(image_sequences, audio_paths)


# # Example city data
# city_data = pd.DataFrame({
#     'Location': ['Hyderabad', 'Bangalore', 'Chennai'],
#     'Latitude': [17.385044, 12.971598, 13.082680],
#     'Longitude': [78.486671, 77.594566, 80.270718]
# })

# generate_weather_video(city_data)

# from PIL import Image, ImageDraw, ImageFont

# # Create a blank white image
# img = Image.new("RGB", (500, 200), "white")
# draw = ImageDraw.Draw(img)

# # Load an emoji-compatible font (Noto Color Emoji)
# emoji_font_path = "/Users/nc25572_mourya/Downloads/Noto_Color_Emoji/NotoColorEmoji-Regular.ttf"

# try:
#     emoji_font = ImageFont.truetype(emoji_font_path, 50)  # Adjust size as needed
#     print(emoji_font)
# except IOError:
#     emoji_font = ImageFont.load_default()

# # Draw text with an emoji
# text = "😃"
# draw.text((50, 75), text, font=emoji_font, fill="black")

# # Save or show the image
# img.show()  # Opens the image to verify
# img.save("emoji_text_image.png")  # Saves the image with emoji text

import cairosvg

svg_text = '''
<svg width="500" height="200" xmlns="http://www.w3.org/2000/svg">
    <text x="50" y="100" font-size="50px" font-family="Noto Color Emoji"></text>
</svg>
'''
cairosvg.svg2png(bytestring=svg_text.encode(), write_to="emoji_text_image.png")
