# import os
# import requests
# import pandas as pd
# import streamlit as st
# from gtts import gTTS
# from moviepy.editor import (AudioFileClip, concatenate_videoclips, ImageClip, CompositeVideoClip)
# from PIL import Image, ImageDraw, ImageFont
# from deep_translator import GoogleTranslator  # For translation
# from langchain_google_genai import ChatGoogleGenerativeAI  # Google Gemini AI

# # API Keys (Replace with your own)
# PEXELS_API_KEY = "S3oSV91Ju3F5RryblOUzpImCDW031bM5xkdzQfiSrKLbdNlB26j1KPWc"
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"
# WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
# GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"  # Replace with your actual API key


# import datetime

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 16:
        return "Good afternoon"
    else:
        return "Good evening"


# # Initialize Google Gemini Chat model
# chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

# # Prompt templates for generating weather advice
prompt_templates = {
    'en': """
        Respond conversationally, offering a very very short weather report, and give a personalized suggestion on how to prepare for the weather.
        The language should be in a very casual manner but polite with simple words that would remain simple after feeding to google translate
        For example:
        - If it's raining, suggest carrying an umbrella or wearing a raincoat.
        - If it's sunny, say that sunlight is there so suggest wearing light coloured clothes.
        - If it's cold, suggest wearing warm clothes like a sweater.
        - If it's windy, suggest a windbreaker or scarf.
        

        Answer:
    """
}

# # Fetch weather data
# def fetch_weather_data(city, latitude, longitude):
#     url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={latitude},{longitude}"
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             temperature = data['current']['temp_c']
#             condition = data['current']['condition']['text']
#             return temperature, condition
#     except Exception:
#         return None, None
#     return None, None

# # Generate weather advice in the selected language
# def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
#     # Add greeting only for the first city
#     if is_first_city:
#         greeting = get_greeting()
#         context = f"{greeting}! The weather in {city} is {temp}°C with {condition}."
#     else:
#         context = f"The weather in {city} is {temp}°C with {condition}."
    
#     prompt = context
#     prompt += prompt_templates.get(lang, prompt_templates['en']).format(context=context)
#     # Generate response using Google Gemini AI or similar service
#     response = chat_model.predict(prompt)
    
#     # Translate if needed
#     if response:
#         if lang != "en":
#             response = GoogleTranslator(source="auto", target=lang).translate(response.strip())
#         return response.strip()
#     return "Stay safe and dress accordingly!"


# # Generate text-to-speech (TTS) audio in the target language
# from pydub import AudioSegment

# # Generate text-to-speech (TTS) audio in the target language
# def generate_audio(city, temp, condition, output_audio_path, lang='en', is_first_city=False, speed_factor=1.2):
#     # Generate weather advice (with greeting for the first city)
#     weather_report = generate_weather_advice(city, temp, condition, lang, is_first_city)
    
#     # Convert the weather report to speech (TTS)
#     try:
#         tts = gTTS(text=weather_report, lang=lang)
#         temp_audio_path = "temp_audio.mp3"
#         tts.save(temp_audio_path)
#         print(f"Audio saved to {temp_audio_path}")

#         # Use pydub to modify the speed of the audio
#         audio = AudioSegment.from_mp3(temp_audio_path)
#         new_audio = audio.speedup(playback_speed=speed_factor)

#         # Save the modified audio to the final output path
#         new_audio.export(output_audio_path, format="mp3")
#         os.remove(temp_audio_path)  # Clean up temporary file
#         print(f"Modified audio saved to {output_audio_path}")
#     except Exception as e:
#         print(f"Error generating or modifying audio: {e}")
    
#     return weather_report


# def download_background_image(weather_condition, save_path="backgrounds"):
#     query = f"field {weather_condition} weather"
#     url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         if "urls" in data:
#             image_url = data["urls"]["full"]  # Get high-quality image URL
#             os.makedirs(save_path, exist_ok=True)
#             image_path = os.path.join(save_path, f"field_{weather_condition}.jpg")

#             try:
#                 img_data = requests.get(image_url).content
#                 with open(image_path, "wb") as img_file:
#                     img_file.write(img_data)
#                 return image_path  # Return saved image path
#             except Exception as e:
#                 print(f"Error saving image: {e}")

#     print(f"Failed to fetch image for {weather_condition}, using fallback image.")
#     return "/Users/nc25572_mourya/Desktop/clear.jpg"



# from PIL import Image, ImageDraw, ImageFont
# import numpy as np

# def create_scrolling_text_pillow(image_clip, city, condition, temp, audio_duration, lang="en", video_size=(640, 360)):
#     # Load language-specific fonts
#     font_path = ""
    
#     if lang == "te":
#         font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Telugu font path
#     elif lang == "hi":
#         font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf"  # Hindi font path
#     elif lang == "kn":
#         font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Kannada/NotoSansKannada-VariableFont_wdth,wght.ttf"  # Kannada font path
#     elif lang == "ml":
#         font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Malayalam/NotoSansMalayalam-VariableFont_wdth,wght.ttf"  # Malayalam font path
#     elif lang == "ta":
#         font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Tamil/NotoSansTamil-VariableFont_wdth,wght.ttf"  # Tamil font path
#     else:
#         font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Default font path (e.g., for English)

#     try:
#         font = ImageFont.truetype(font_path, 30)
#     except IOError:
#         font = ImageFont.load_default()

#     image = image_clip.get_frame(0)
#     pil_image = Image.fromarray(image)
#     draw = ImageDraw.Draw(pil_image)
    
#     # Translate text if needed
#     text = f"{city}: {condition}, {temp}°C"
#     if lang != "en":
#         text = GoogleTranslator(source="auto", target=lang).translate(text)
        
#     # Calculate text bounding box
#     bbox = draw.textbbox((0, 0), text, font=font)
#     text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

#     # Adjust scrolling speed
#     if audio_duration > 6:
#         num_scrolls = 2  # Ensure two full scrolls
#     else:
#         num_scrolls = 1  # One full scroll

#     total_distance = num_scrolls * (video_size[0] + text_width)
#     speed = total_distance / audio_duration  # Pixels per second
#     vertical_center = video_size[1] - 50  # 50px from the bottom

#     def update_frame(t):
#         img = pil_image.copy()
#         draw = ImageDraw.Draw(img)

#         # Calculate the x_offset for looping effect
#         x_offset = int(video_size[0] - (t * speed)) % (video_size[0] + text_width)

#         # Draw the text twice to create a seamless looping effect
#         draw.text((x_offset, vertical_center), text, font=font, fill="white")

#         # Draw the second instance of text slightly ahead of the first one
#         draw.text((x_offset - (video_size[0] + text_width), vertical_center), text, font=font, fill="white")

#         return np.array(img)

#     return update_frame, audio_duration



# # Create a video clip
# def create_video_clip(image_file, audio_file, city, condition, temp, lang="en", video_size=(640, 360)):
#     image_clip = ImageClip(image_file).resize(video_size)
#     try:
#         audio_clip = AudioFileClip(audio_file)
#     except Exception:
#         print(f"Error loading audio: {audio_file}")
#         return None
#     image_clip = image_clip.set_duration(audio_clip.duration)

#     update_frame, audio_duration = create_scrolling_text_pillow(image_clip, city, condition, temp, audio_clip.duration, lang=lang, video_size=video_size)
#     video_clip = image_clip.fl(lambda gf, t: update_frame(t))
#     final_clip = CompositeVideoClip([video_clip.set_audio(audio_clip)])
#     return final_clip

# # Process CSV file and generate video
# def process_csv(csv_file, lang='en', output_path="output"):
#     os.makedirs(output_path, exist_ok=True)
#     df = pd.read_csv(csv_file)

#     if not {'location', 'latitude', 'longitude'}.issubset(df.columns):
#         st.error("CSV must contain 'location', 'latitude', and 'longitude' columns.")
#         return []

#     clips = []
#     is_first_city = True  # Flag to track the first city

#     for idx, row in df.iterrows():
#         city, lat, lon = row['location'], row['latitude'], row['longitude']
#         temp, condition = fetch_weather_data(city, lat, lon)
#         if temp is None or condition is None:
#             continue

#         background_image = download_background_image(condition)

#         audio_path = f"{output_path}/{city}_weather.mp3"
        
#         generate_audio(city, temp, condition, audio_path, lang, is_first_city, speed_factor = 1.2)

#         clip = create_video_clip(background_image, audio_path, city, condition, temp, lang=lang)
#         if clip and clip.duration > 0:
#             clips.append(clip)

#         is_first_city = False

#     if clips:
#         final_video_path = os.path.join(output_path, f"weather_report_{lang}.mp4")
#         final_video = concatenate_videoclips(clips, method="compose")
#         final_video.write_videofile(final_video_path, fps=24, codec="libx264", audio_codec="aac")
#         return final_video_path
#     return None


# # Streamlit UI
# st.title("🌦️ Weather Report Video Generator")
# st.write("Upload a CSV file containing **location, latitude, and longitude**, select a language, and generate a weather video.")

# uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

# language_options = {"English": "en", "Telugu": "te", "Hindi": "hi", "Malayalam": "ml", "Kannada": "kn", "tamil": "ta"}
# selected_lang = st.selectbox("Select Language", list(language_options.keys()))

# if st.button("Generate Video"):
#     if uploaded_file is not None:
#         st.write("Processing your weather report...")
#         with open("uploaded_data.csv", "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         output_video_path = process_csv("uploaded_data.csv", lang=language_options[selected_lang])

#         if output_video_path:
#             st.video(output_video_path)
#             st.success("Video generated successfully!")

#             with open(output_video_path, "rb") as video_file:
#                 st.download_button(
#                     label="Download Video",
#                     data=video_file,
#                     file_name=os.path.basename(output_video_path),
#                     mime="video/mp4"
#                 )
#         else:
#             st.error("Failed to generate video. Please try again.")
#     else:
#         st.error("Please upload a CSV file first.")


# import os
# import pandas as pd
# import requests
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips

# def fetch_weather(api_key, lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# def generate_image(location, temperature, condition, index):
#     img = Image.new('RGB', (1280, 720), color=(135, 206, 250))  # Light blue background
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.load_default()
#     text = f"Weather Report for {location}\nTemperature: {temperature}°C\nCondition: {condition}"
#     draw.text((50, 300), text, fill='black', font=font)
#     img_path = f"frame_{index}.png"
#     img.save(img_path)
#     return img_path

# def generate_audio(text, index):
#     tts = gTTS(text=text, lang='en')
#     audio_path = f"audio_{index}.mp3"
#     tts.save(audio_path)
#     return audio_path

# def create_video(image_paths, audio_paths, output_file="weather_report.mp4"):
#     clip = ImageSequenceClip(image_paths, fps=1)
#     audio_clips = [AudioFileClip(audio) for audio in audio_paths]
#     final_audio = concatenate_audioclips(audio_clips)
#     clip = clip.set_audio(final_audio)
#     clip.write_videofile(output_file, codec="libx264", fps=1)

# def main(csv_file, api_key):
#     df = pd.read_csv(csv_file)
#     image_paths, audio_paths = [], []
    
#     for index, row in df.iterrows():
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
#         weather_data = fetch_weather(api_key, lat, lon)
#         if weather_data:
#             temp = weather_data['main']['temp']
#             condition = weather_data['weather'][0]['description'].title()
#             image_path = generate_image(location, temp, condition, index)
#             audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#             audio_path = generate_audio(audio_text, index)
#             image_paths.append(image_path)
#             audio_paths.append(audio_path)
    
#     create_video(image_paths, audio_paths)
    
#     # Cleanup
#     for file in image_paths + audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "locations.csv"  # Replace with your actual CSV file
#     api_key = "your_openweathermap_api_key"  # Replace with your API key
#     main(csv_file, api_key)


# import os
# import pandas as pd
# import requests
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips
# import folium
# import time
# from selenium import webdriver

# # Function to fetch weather details from OpenWeatherMap API
# def fetch_weather(api_key, lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # Function to create map, save it as an image, and add weather details
# def create_map(lat, lon, city_name):
#     map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)
    
#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
    
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load
    
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     return screenshot_path

# # Function to generate image with weather details and map
# def generate_image_with_map(location, temperature, condition, lat, lon, index):
#     # Create map image
#     map_image = create_map(lat, lon, location)
    
#     # Load the map image as background
#     img = Image.open(map_image)
#     draw = ImageDraw.Draw(img)
    
#     # Use a system font for the weather text
#     font = ImageFont.load_default()
#     text = f"Weather Report for {location}\nTemperature: {temperature}°C\nCondition: {condition}"
    
#     # Adjust the position and add the weather details on the map
#     draw.text((50, 300), text, fill='black', font=font)
    
#     # Save the image with weather details
#     img_path = f"frame_{index}.png"
#     img.save(img_path)
#     return img_path

# # Function to generate audio for the weather report
# def generate_audio(text, index):
#     tts = gTTS(text=text, lang='en')
#     audio_path = f"audio_{index}.mp3"
#     tts.save(audio_path)
#     return audio_path

# # Function to create the video with image and audio
# def create_video(image_paths, audio_paths, output_file="weather_report.mp4"):
#     clip = ImageSequenceClip(image_paths, fps=1)
#     audio_clips = [AudioFileClip(audio) for audio in audio_paths]
#     final_audio = concatenate_audioclips(audio_clips)
#     clip = clip.set_audio(final_audio)
#     clip.write_videofile(output_file, codec="libx264", fps=1)

# # Main function to process CSV, fetch weather, and generate video
# def main(csv_file, api_key):
#     df = pd.read_csv(csv_file)
#     image_paths, audio_paths = [], []
    
#     # Loop through each city in the CSV and generate map, weather report, image, and audio
#     for index, row in df.iterrows():
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
#         weather_data = fetch_weather(api_key, lat, lon)
        
#         if weather_data:
#             temp = weather_data['main']['temp']
#             condition = weather_data['weather'][0]['description'].title()
            
#             # Generate image with map and weather details
#             image_path = generate_image_with_map(location, temp, condition, lat, lon, index)
            
#             # Generate audio for the weather report
#             audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#             audio_path = generate_audio(audio_text, index)
            
#             image_paths.append(image_path)
#             audio_paths.append(audio_path)
    
#     # Create a video from the generated images and audio
#     create_video(image_paths, audio_paths)
    
#     # Cleanup temporary files
#     for file in image_paths + audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"  # Replace with your actual CSV file
#     api_key = "22cd9db3340944d697b173414252401"  # Replace with your API key
#     main(csv_file, api_key)



# import os
# import pandas as pd
# import requests
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips
# import folium
# import time
# from selenium import webdriver

# # Function to fetch weather details from WeatherAPI
# def fetch_weather(api_key, lat, lon):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # Function to create map, save it as an image, and add weather details
# def create_map(lat, lon, city_name):
#     map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)
    
#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
    
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load
    
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     return screenshot_path

# # Function to generate image with weather details and map
# def generate_image_with_map(location, temperature, condition, lat, lon, index):
#     # Create map image
#     map_image = create_map(lat, lon, location)
    
#     # Load the map image as background
#     img = Image.open(map_image)
#     draw = ImageDraw.Draw(img)
    
#     # Use a system font for the weather text
#     font = ImageFont.load_default()
#     text = f"Weather Report for {location}\nTemperature: {temperature}°C\nCondition: {condition}"
    
#     # Adjust the position and add the weather details on the map
#     draw.text((50, 300), text, fill='black', font=font)
    
#     # Save the image with weather details
#     img_path = f"frame_{index}.png"
#     img.save(img_path)
#     return img_path

# # Function to generate audio for the weather report
# def generate_audio(text, index):
#     tts = gTTS(text=text, lang='en')
#     audio_path = f"audio_{index}.mp3"
#     tts.save(audio_path)
#     return audio_path

# # Function to create the video with image and audio
# def create_video(image_paths, audio_paths, output_file="weather_report.mp4"):
#     clip = ImageSequenceClip(image_paths, fps=1)
#     audio_clips = [AudioFileClip(audio) for audio in audio_paths]
#     final_audio = concatenate_audioclips(audio_clips)
#     clip = clip.set_audio(final_audio)
#     clip.write_videofile(output_file, codec="libx264", fps=1)

# # Main function to process CSV, fetch weather, and generate video
# def main(csv_file, api_key):
#     df = pd.read_csv(csv_file)
    
#     # Check if the necessary columns are in the CSV
#     if 'location' not in df.columns or 'latitude' not in df.columns or 'longitude' not in df.columns:
#         print("CSV file does not contain the required columns: 'location', 'latitude', 'longitude'")
#         return

#     df = df.dropna(subset=['location', 'latitude', 'longitude'])  # Remove rows with missing data

#     image_paths, audio_paths = [], []
    
#     # Loop through each city in the CSV and generate map, weather report, image, and audio
#     for index, row in df.iterrows():
#         print(f"Processing row {index}: {row}")  # Debugging: Print each row being processed
        
#         if pd.isnull(row['location']) or pd.isnull(row['latitude']) or pd.isnull(row['longitude']):
#             print(f"Skipping row {index} due to missing data.")
#             continue  # Skip this row if any data is missing
        
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
        
#         weather_data = fetch_weather(api_key, lat, lon)
        
#         if weather_data:
#             # Extract the weather data using the updated API response structure
#             if 'current' in weather_data and 'condition' in weather_data['current']:
#                 temp = weather_data['current']['temp_c']
#                 condition = weather_data['current']['condition']['text']
                
#                 # Generate image with map and weather details
#                 image_path = generate_image_with_map(location, temp, condition, lat, lon, index)
                
#                 # Generate audio for the weather report
#                 audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#                 audio_path = generate_audio(audio_text, index)
                
#                 image_paths.append(image_path)
#                 audio_paths.append(audio_path)
#             else:
#                 print(f"Missing current weather data for {location}. Skipping this location.")
#         else:
#             print(f"Failed to fetch weather data for {location}. Skipping this location.")
    
#     # Create a video from the generated images and audio
#     create_video(image_paths, audio_paths)
    
#     # Cleanup temporary files
#     for file in image_paths + audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"  # Replace with your actual CSV file
#     api_key = "22cd9db3340944d697b173414252401"  # Replace with your API key
#     main(csv_file, api_key)


# import os
# import pandas as pd
# import requests
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips
# import folium
# import time
# from selenium import webdriver

# # Unsplash API Key
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"

# # Function to fetch weather details from WeatherAPI
# def fetch_weather(api_key, lat, lon):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # Function to create map, save it as an image, and add weather details
# def create_map(lat, lon, city_name):
#     map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)
    
#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
    
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load
    
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     return screenshot_path

# # Function to download background image based on weather condition
# def download_background_image(weather_condition, city, save_path="backgrounds"):
#     query = f"farm {city}"
#     print(city)
#     url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    
#     response = requests.get(url)

#     print(response)


#     if response.status_code == 200:
#         data = response.json()

#         # Check if 'data' is a list and not empty
#         # if isinstance(data, list) and len(data) > 0 and "urls" in data[0]:
#         #     image_url = data[0]["urls"]["full"]
#             # os.makedirs(save_path, exist_ok=True)
#             # image_path = os.path.join(save_path, f"weather_{weather_condition}.jpg")
            
#         #     try:
#                 # img_data = requests.get(image_url).content
#                 # with open(image_path, "wb") as img_file:
#                 #     img_file.write(img_data)
#                 # return image_path
#         #     except Exception as e:
#         #         print(f"Error saving image: {e}")

#         image_url = data['urls']['raw']
#         os.makedirs(save_path, exist_ok=True)
#         image_path = os.path.join(save_path, f"weather_{weather_condition}.jpg")
#         img_data = requests.get(image_url).content
#         with open(image_path, "wb") as img_file:
#             img_file.write(img_data)
#             return image_path
#         # else:
#         #     print(f"No image found for the query '{weather_condition}' or invalid data.")
#     else:
#         print(f"Failed to fetch data from Unsplash API. Status code: {response.status_code}")

#     print(f"Using fallback image for {weather_condition}.")
#     return "/Users/nc25572_mourya/Desktop/clear.jpg"  # Fallback image path



# # Function to generate image with weather details and background image
# STANDARD_SIZE = (1280, 720)  # Set a fixed resolution for all images

# def generate_image_with_background(location, temperature, condition, lat, lon, weather_condition, index):
#     # Download background image
#     background_image = download_background_image(weather_condition, location)
    
#     # Open background image
#     bg_img = Image.open(background_image).convert("RGB")
#     bg_img = bg_img.resize(STANDARD_SIZE)  # Ensure a uniform size

#     # Create map image
#     map_image = create_map(lat, lon, location)
    
#     # Open and resize the map image
#     map_img = Image.open(map_image).convert("RGB")
#     map_img = map_img.resize(STANDARD_SIZE)  # Ensure the same size
    
#     # Merge map onto background
#     final_img = Image.blend(bg_img, map_img, alpha=0.5)  # Blend images (adjust alpha as needed)
    
#     # Add weather text
#     draw = ImageDraw.Draw(final_img)
#     font = ImageFont.load_default()
#     text = f"Weather in {location}\nTemperature: {temperature}°C\nCondition: {condition}"
    
#     draw.text((50, 50), text, fill="black", font=font)

#     # Save final image
#     img_path = f"frame_{index}.png"
#     final_img.save(img_path)
    
#     return img_path

# # Function to generate audio for the weather report
# def generate_audio(text, index):
#     tts = gTTS(text=text, lang='en')
#     audio_path = f"audio_{index}.mp3"
#     tts.save(audio_path)
#     return audio_path

# # Function to create the video with image and audio
# def create_video(image_paths, audio_paths, output_file="weather_report.mp4"):
#     clip = ImageSequenceClip(image_paths, fps=1)
#     audio_clips = [AudioFileClip(audio) for audio in audio_paths]
#     final_audio = concatenate_audioclips(audio_clips)
#     clip = clip.set_audio(final_audio)
#     clip.write_videofile(output_file, codec="libx264", fps=1)

# # Main function to process CSV, fetch weather, and generate video
# def main(csv_file, api_key):
#     df = pd.read_csv(csv_file)
    
#     # Check if the necessary columns are in the CSV
#     if 'location' not in df.columns or 'latitude' not in df.columns or 'longitude' not in df.columns:
#         print("CSV file does not contain the required columns: 'location', 'latitude', 'longitude'")
#         return

#     df = df.dropna(subset=['location', 'latitude', 'longitude'])  # Remove rows with missing data

#     image_paths, audio_paths = [], []
    
#     # Loop through each city in the CSV and generate map, weather report, image, and audio
#     for index, row in df.iterrows():
#         print(f"Processing row {index}: {row}")  # Debugging: Print each row being processed
        
#         if pd.isnull(row['location']) or pd.isnull(row['latitude']) or pd.isnull(row['longitude']):
#             print(f"Skipping row {index} due to missing data.")
#             continue  # Skip this row if any data is missing
        
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
        
#         weather_data = fetch_weather(api_key, lat, lon)
        
#         if weather_data:
#             # Extract the weather data using the updated API response structure
#             if 'current' in weather_data and 'condition' in weather_data['current']:
#                 temp = weather_data['current']['temp_c']
#                 condition = weather_data['current']['condition']['text']
                
#                 # Generate image with map and weather details
#                 image_path = generate_image_with_background(location, temp, condition, lat, lon, condition, index)
                
#                 # Generate audio for the weather report
#                 audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#                 audio_path = generate_audio(audio_text, index)
                
#                 image_paths.append(image_path)
#                 audio_paths.append(audio_path)
#             else:
#                 print(f"Missing current weather data for {location}. Skipping this location.")
#         else:
#             print(f"Failed to fetch weather data for {location}. Skipping this location.")
    
#     # Create a video from the generated images and audio
#     create_video(image_paths, audio_paths)
    
#     # Cleanup temporary files
#     for file in image_paths + audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"  # Replace with your actual CSV file
#     api_key = "22cd9db3340944d697b173414252401"  # Replace with your API key
#     main(csv_file, api_key)


# import os
# import pandas as pd
# import requests
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips
# import folium
# import time
# from selenium import webdriver

# # Unsplash API Key
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"

# # Function to fetch weather details from WeatherAPI
# def fetch_weather(api_key, lat, lon):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # Function to create map, save it as an image, and add weather details
# def create_map(lat, lon, city_name):
#     map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)
    
#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
    
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load
    
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     return screenshot_path

# # Function to download background image based on weather condition
# def download_background_image(city, save_path="backgrounds"):
#     query = f"farm {city}"
#     url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         if "urls" in data:
#             image_url = data["urls"]["raw"]
#             os.makedirs(save_path, exist_ok=True)
#             image_path = os.path.join(save_path, f"{city}.jpg")
#             img_data = requests.get(image_url).content
#             with open(image_path, "wb") as img_file:
#                 img_file.write(img_data)
#             return image_path

#     print(f"Using fallback image for {city}.")
#     return "/Users/nc25572_mourya/Desktop/clear.jpg"  # Fallback image path

# # Function to add text overlay on images
# def add_text_overlay(image_path, text):
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize((1280, 720))  # Standard size
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.load_default()
#     draw.text((50, 50), text, fill="black", font=font)
    
#     output_path = f"overlay_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path

# # Function to generate audio for the weather report
# def generate_audio(text, index):
#     tts = gTTS(text=text, lang='en')
#     audio_path = f"audio_{index}.mp3"
#     tts.save(audio_path)
#     return audio_path

# # Function to create the video with image and audio
# def create_video(image_paths, audio_paths, output_file="weather_report.mp4"):
#     clip = ImageSequenceClip(image_paths, fps=1)
#     audio_clips = [AudioFileClip(audio) for audio in audio_paths]
#     final_audio = concatenate_audioclips(audio_clips)
#     clip = clip.set_audio(final_audio)
#     clip.write_videofile(output_file, codec="libx264", fps=1)

# # Main function to process CSV, fetch weather, and generate video
# def main(csv_file, api_key):
#     df = pd.read_csv(csv_file)
    
#     if 'location' not in df.columns or 'latitude' not in df.columns or 'longitude' not in df.columns:
#         print("CSV file does not contain the required columns: 'location', 'latitude', 'longitude'")
#         return

#     df = df.dropna(subset=['location', 'latitude', 'longitude'])

#     image_paths, audio_paths = [], []
    
#     for index, row in df.iterrows():
#         print(f"Processing row {index}: {row}")
        
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
        
#         weather_data = fetch_weather(api_key, lat, lon)
        
#         if weather_data and 'current' in weather_data and 'condition' in weather_data['current']:
#             temp = weather_data['current']['temp_c']
#             condition = weather_data['current']['condition']['text']
            
#             # Step 1: Generate map image
#             map_image = create_map(lat, lon, location)
#             map_image_with_text = add_text_overlay(map_image, f"Location: {location}\nTemperature: {temp}°C\nCondition: {condition}")
#             image_paths.append(map_image_with_text)
            
#             # Step 2: Generate background image with weather report
#             background_image = download_background_image(location)
#             weather_report_image = add_text_overlay(background_image, f"Weather in {location}\nTemperature: {temp}°C\nCondition: {condition}")
#             image_paths.append(weather_report_image)
            
#             # Step 3: Generate audio for the weather report
#             audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#             audio_path = generate_audio(audio_text, index)
#             audio_paths.append(audio_path)
#         else:
#             print(f"Failed to fetch weather data for {location}. Skipping this location.")
    
#     create_video(image_paths, audio_paths)
    
#     # Cleanup temporary files
#     for file in image_paths + audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"
#     api_key = "22cd9db3340944d697b173414252401"
#     main(csv_file, api_key)


# import os
# import pandas as pd
# import requests
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips, concatenate_videoclips
# import folium
# import time
# from selenium import webdriver

# # Unsplash API Key
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"

# # Function to fetch weather details from WeatherAPI
# def fetch_weather(api_key, lat, lon):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     return None

# # Function to create map and save it as an image
# def create_map(lat, lon, city_name):
#     map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)
    
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
    
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load
    
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     return screenshot_path

# # Function to download background image based on city
# def download_background_image(city, save_path="backgrounds"):
#     query = f"farm {city}"
#     url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}"
    
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         if "urls" in data:
#             image_url = data["urls"]["raw"]
#             os.makedirs(save_path, exist_ok=True)
#             image_path = os.path.join(save_path, f"{city}.jpg")
#             img_data = requests.get(image_url).content
#             with open(image_path, "wb") as img_file:
#                 img_file.write(img_data)
#             return image_path

#     print(f"Using fallback image for {city}.")
#     return "/Users/nc25572_mourya/Desktop/clear.jpg"  # Fallback image path

# # Function to add text overlay to images
# def add_text_overlay(image_path, text):
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize((1280, 720))  # Standard size
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.load_default()
#     draw.text((50, 50), text, fill="black", font=font)
    
#     output_path = f"overlay_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path

# # Function to generate audio for the weather report
# def generate_audio(text, index):
#     tts = gTTS(text=text, lang='te')
#     audio_path = f"audio_{index}.mp3"
#     tts.save(audio_path)
#     return audio_path

# # Function to create the video sequence
# def create_video(image_sequences, audio_paths, output_file="weather_report.mp4"):
#     final_clips = []
    
#     for images, audio in zip(image_sequences, audio_paths):
#         audio_clip = AudioFileClip(audio)
#         duration = audio_clip.duration
        
#         # First 2 seconds: Show map image
#         map_clip = ImageSequenceClip([images[0]], durations=[2])
        
#         # Remaining time: Show background image
#         background_clip = ImageSequenceClip([images[1]], durations=[duration - 2])
        
#         # Merge clips
#         video_clip = concatenate_videoclips([map_clip, background_clip])
#         video_clip = video_clip.set_audio(audio_clip)
        
#         final_clips.append(video_clip)
    
#     # Combine all city clips
#     final_video = concatenate_videoclips(final_clips)
#     final_video.write_videofile(output_file, codec="libx264", fps=1)

# # Main function to process CSV and generate video
# def main(csv_file, api_key):
#     df = pd.read_csv(csv_file)
    
#     if 'location' not in df.columns or 'latitude' not in df.columns or 'longitude' not in df.columns:
#         print("CSV file does not contain the required columns: 'location', 'latitude', 'longitude'")
#         return

#     df = df.dropna(subset=['location', 'latitude', 'longitude'])

#     image_sequences, audio_paths = [], []
    
#     for index, row in df.iterrows():
#         print(f"Processing row {index}: {row}")
        
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
        
#         weather_data = fetch_weather(api_key, lat, lon)
        
#         if weather_data and 'current' in weather_data and 'condition' in weather_data['current']:
#             temp = weather_data['current']['temp_c']
#             condition = weather_data['current']['condition']['text']
            
#             # Generate map image
#             map_image = create_map(lat, lon, location)
#             map_image_with_text = add_text_overlay(map_image, f"Location: {location}\nTemperature: {temp}°C\nCondition: {condition}")
            
#             # Generate background image with weather details
#             background_image = download_background_image(location)
#             weather_report_image = add_text_overlay(background_image, f"Weather in {location}\nTemperature: {temp}°C\nCondition: {condition}")
            
#             # Generate audio for the weather report
#             audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#             audio_path = generate_audio(audio_text, index)
            
#             # Store images and audio
#             image_sequences.append([map_image_with_text, weather_report_image])
#             audio_paths.append(audio_path)
#         else:
#             print(f"Failed to fetch weather data for {location}. Skipping this location.")
    
#     create_video(image_sequences, audio_paths)
    
#     # Cleanup temporary files
#     for images in image_sequences:
#         for file in images:
#             os.remove(file)
    
#     for file in audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"
#     api_key = "22cd9db3340944d697b173414252401"
#     main(csv_file, api_key)


# import os
# import time
# import datetime
# import requests
# import pandas as pd
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

# # API Keys (Replace with your own)
# WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"
# GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"

# # Initialize Google Gemini Chat model
# chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

# # Get time-based greeting
# def get_greeting():
#     current_hour = datetime.datetime.now().hour
#     if current_hour < 12:
#         return "Good morning"
#     elif 12 <= current_hour < 18:
#         return "Good afternoon"
#     else:
#         return "Good evening"

# # Fetch weather details from WeatherAPI
# def fetch_weather(api_key, lat, lon):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data['current']['temp_c'], data['current']['condition']['text']
#     return None, None

# # Generate weather advice using AI & translate it
# def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
#     greeting = get_greeting() if is_first_city else ""
#     context = f"{greeting} The weather in {city} is {temp}°C with {condition}."

#     # Generate AI-based advice
#     prompt = f"""{context}
#     Give a very short 1-2 lines, friendly weather suggestion:
#     - If it's raining, suggest carrying an umbrella.
#     - If it's sunny, suggest wearing light-colored clothes.
#     - If it's cold, suggest wearing warm clothes.
#     - If it's windy, suggest wearing a scarf or windbreaker.
#     """
#     response = chat_model.predict(prompt).strip()

#     # Translate if needed
#     if lang != "en":
#         response = GoogleTranslator(source="auto", target=lang).translate(response)
    
#     return response

# # Generate text-to-speech (TTS) audio
# # Generate text-to-speech (TTS) audio with varied descriptions
# def generate_audio(city, temp, condition, output_audio_path, lang='en', is_first_city=False):
#     greeting = get_greeting() + "! " if is_first_city else ""
    
#     # AI-generated varied description
#     prompt = f"""{greeting} The weather in {city} is {temp}°C with {condition}. It's a great day to enjoy the outdoors!

#     Example styles:
#     - "{city}: {temp}°C and sunny, perfect for a walk!"
#     - "{city} feels cozy with {temp}°C, a nice day for some relaxation."
#     - "A pleasant {temp}°C in {city} today, ideal for a quick stroll."

#     Finish with a weather tip based on the condition."""

    
#     response = chat_model.predict(prompt).strip()

#     # Translate if needed
#     if lang != "en":
#         response = GoogleTranslator(source="auto", target=lang).translate(response)
    
    # try:
    #     tts = gTTS(text=response, lang=lang)
    #     temp_audio_path = "temp_audio.mp3"
    #     tts.save(temp_audio_path)

    #     # Modify speed using pydub
    #     audio = AudioSegment.from_mp3(temp_audio_path)
    #     new_audio = audio.speedup(playback_speed=1.2)
    #     new_audio.export(output_audio_path, format="mp3")
    #     os.remove(temp_audio_path)
    # except Exception as e:
    #     print(f"Error generating audio: {e}")
    
    # return response


# # Create a map image with a marker
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

# # Download background image from Unsplash
# # Download different images for each city based on weather
# def download_background_image(city, weather_condition, save_path="backgrounds"):
#     os.makedirs(save_path, exist_ok=True)
    
#     query = f"farm with {weather_condition}"
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
#             return image_path

#     return "/Users/nc25572_mourya/Desktop/clear.jpg"  # Fallback image

# # Add text overlay to image
# def add_text_overlay(image_path, text):
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize((720, 540))
#     draw = ImageDraw.Draw(img)
#     # font = ImageFont.truetype("path_to_font.ttf", size=40)
#     font = ImageFont.load_default()
#     draw.text((50, 50), text, fill="black", font=font)

#     output_path = f"overlay_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path

# # Create video sequence
# def create_video(image_sequences, audio_paths, output_file="weather_report.mp4"):
#     final_clips = []
    
#     for images, audio in zip(image_sequences, audio_paths):
#         audio_clip = AudioFileClip(audio)
#         duration = audio_clip.duration

#         # First 2 seconds: Show map image
#         map_clip = ImageSequenceClip([images[0]], durations=[2])
        
#         # Remaining time: Show background image
#         background_clip = ImageSequenceClip([images[1]], durations=[duration - 2])
        
#         # Merge clips
#         video_clip = concatenate_videoclips([map_clip, background_clip])
#         video_clip = video_clip.set_audio(audio_clip)
        
#         final_clips.append(video_clip)
    
#     final_video = concatenate_videoclips(final_clips)
#     final_video.write_videofile(output_file, codec="libx264", fps=1)

# # Main function to process CSV and generate video
# def main(csv_file, api_key, lang="en"):
#     df = pd.read_csv(csv_file)
    
#     if 'location' not in df.columns or 'latitude' not in df.columns or 'longitude' not in df.columns:
#         print("CSV file is missing required columns: 'location', 'latitude', 'longitude'")
#         return

#     df = df.dropna(subset=['location', 'latitude', 'longitude'])

#     image_sequences, audio_paths = [], []
    
#     for index, row in df.iterrows():
#         print(f"Processing {row['location']}...")
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
        
#         temp, condition = fetch_weather(api_key, lat, lon)
#         if temp is None or condition is None:
#             print(f"Failed to fetch weather data for {location}. Skipping.")
#             continue
        
#         # Generate images
#         map_image = create_map(lat, lon, location)
#         background_image = download_background_image(location, condition)
        
#         # Add text overlay
#         map_image_with_text = add_text_overlay(map_image, f"{location}\n{temp}°C, {condition}")
#         weather_report_image = add_text_overlay(background_image, f"Weather in {location}\n{temp}°C, {condition}")
        
#         # Generate audio
#         is_first_city = index == 0
#         audio_path = f"audio_{index}.mp3"
#         generate_audio(location, temp, condition, audio_path, lang, is_first_city)
        
#         # Store data for video generation
#         image_sequences.append([map_image_with_text, weather_report_image])
#         audio_paths.append(audio_path)

#     create_video(image_sequences, audio_paths)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"
#     main(csv_file, WEATHER_API_KEY, lang="te")  # Change language as needed



# import os
# import time
# import datetime
# import requests
# import pandas as pd
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
# import numpy as np

# # API Keys (Replace with your own)
# WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"
# GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"

# # Initialize Google Gemini Chat model
# chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

# # Get time-based greeting
# def get_greeting():
#     current_hour = datetime.datetime.now().hour
#     if current_hour < 12:
#         return "Good morning"
#     elif 12 <= current_hour < 18:
#         return "Good afternoon"
#     else:
#         return "Good evening"

# # Fetch weather details from WeatherAPI
# def fetch_weather(api_key, lat, lon):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data['current']['temp_c'], data['current']['condition']['text']
#     return None, None

# # Generate weather advice using AI & translate it
# # def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
# #     greeting = get_greeting() if is_first_city else ""
# #     context = f"{greeting} The weather in {city} is {temp}°C with {condition}."

# #     # Generate AI-based advice
# #     prompt = f"""{context}
# #     Give a very short 1-2 lines, friendly weather suggestion:
# #     - If it's raining, suggest carrying an umbrella.
# #     - If it's sunny, suggest wearing light-colored clothes.
# #     - If it's cold, suggest wearing warm clothes.
# #     - If it's windy, suggest wearing a scarf or windbreaker.
# #     """
# #     response = chat_model.predict(prompt).strip()

# #     # Translate if needed
# #     if lang != "en":
# #         response = GoogleTranslator(source="auto", target=lang).translate(response)
    
# #     return response


# def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
#     greeting = get_greeting() if is_first_city else ""
#     context = f"{city}: {temp}°C, {condition}."
    
#     # Generate AI-based advice in one short sentence
#     prompt = f"""{context} 
#     Give a very short and clear weather suggestion in one sentence. 
#     Example: "Carry an umbrella if it rains." or "Wear warm clothes if it's cold."
#     """
#     response = chat_model.predict(prompt).strip()

#     if lang != "en":
#         response = GoogleTranslator(source="auto", target=lang).translate(response)
    
#     return f"{context} {response}"


# # Create scrolling text
# def create_scrolling_text_pillow(image_clip, city, condition, temp, audio_duration, lang="en", video_size=(640, 360)):
#     # Load language-specific fonts
    # font_path = ""
    
    # if lang == "te":
    #     font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Telugu font path
    # elif lang == "hi":
    #     font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf"  # Hindi font path
    # elif lang == "kn":
    #     font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Kannada/NotoSansKannada-VariableFont_wdth,wght.ttf"  # Kannada font path
    # elif lang == "ml":
    #     font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Malayalam/NotoSansMalayalam-VariableFont_wdth,wght.ttf"  # Malayalam font path
    # elif lang == "ta":
    #     font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Tamil/NotoSansTamil-VariableFont_wdth,wght.ttf"  # Tamil font path
    # else:
    #     font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Default font path (e.g., for English)

#     try:
#         font = ImageFont.truetype(font_path, 30)
#     except IOError:
#         font = ImageFont.load_default()

#     image = image_clip.get_frame(0)
#     pil_image = Image.fromarray(image)
#     draw = ImageDraw.Draw(pil_image)
    
#     # Translate text if needed
#     text = f"{city}: {condition}, {temp}°C"
#     if lang != "en":
#         text = GoogleTranslator(source="auto", target=lang).translate(text)
        
#     # Calculate text bounding box
#     bbox = draw.textbbox((0, 0), text, font=font)
#     text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

#     # Adjust scrolling speed
#     # Adjust text scrolling speed and duration for better stability
#     if audio_duration > 5:
#         num_scrolls = 1  # Reduce excessive scrolling
#     else:
#         num_scrolls = 1  # Keep it stable

#     total_distance = (video_size[0] + text_width)
#     speed = total_distance / audio_duration  # Pixels per second

#     vertical_center = video_size[1] - 50  # 50px from the bottom

#     def update_frame(t):
#         img = pil_image.copy()
#         draw = ImageDraw.Draw(img)

#         # Calculate the x_offset for looping effect
#         x_offset = int(video_size[0] - (t * speed)) % (video_size[0] + text_width)

#         # Draw the text twice to create a seamless looping effect
#         draw.text((x_offset, vertical_center), text, font=font, fill="white")

#         # Draw the second instance of text slightly ahead of the first one
#         draw.text((x_offset - (video_size[0] + text_width), vertical_center), text, font=font, fill="white")

#         return np.array(img)

#     return update_frame, audio_duration

# # Create a map image with a marker
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

# # Download background image from Unsplash
# # Download different images for each city based on weather
# def download_background_image(city, weather_condition, save_path="backgrounds"):
#     os.makedirs(save_path, exist_ok=True)
    
#     query = f"farm with {weather_condition}"
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
#             return image_path

#     return "/Users/nc25572_mourya/Desktop/clear.jpg"  # Fallback image

# # Add text overlay to image
# def add_text_overlay(image_path, text):
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize((720, 540))
#     draw = ImageDraw.Draw(img)
#     # font = ImageFont.truetype("path_to_font.ttf", size=40)
#     font = ImageFont.load_default()
#     draw.text((50, 50), text, fill="black", font=font)

#     output_path = f"overlay_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path


# # Generate audio from text using Google Text-to-Speech
# def generate_audio(text, lang="en"):
#     tts = gTTS(text=text, lang=lang, slow=False)
#     audio_file = "weather_advice.mp3"
#     tts.save(audio_file)
    
#     # Optionally, you can convert the audio to a different format or process it (e.g., adjust volume, speed)
#     return audio_file


# # Create video sequence
# def create_video(image_sequences, audio_paths, output_file="weather_report.mp4"):
#     final_clips = []
    
#     for images, audio in zip(image_sequences, audio_paths):
#         audio_clip = AudioFileClip(audio)
#         duration = audio_clip.duration

#         # First 2 seconds: Show map image
#         map_clip = ImageSequenceClip([images[0]], durations=[2])
        
#         # Remaining time: Show background image with scrolling text
#         background_clip = ImageSequenceClip([images[1]], durations=[duration - 2])
        
#         # Add crossfade transition between clips for smoother effect
#         video_clip = concatenate_videoclips([map_clip, background_clip], method="compose").crossfadein(1)

#         video_clip = video_clip.set_audio(audio_clip)
        
#         final_clips.append(video_clip)
    
#     final_video = concatenate_videoclips(final_clips)
#     final_video.write_videofile(output_file, codec="libx264", fps=24)

# # Main function to process cities and generate weather video
# def generate_weather_video(city_data):
#     image_sequences = []
#     audio_paths = []

#     for index, row in city_data.iterrows():
#         city_name = row['Location']
#         lat, lon = row['Latitude'], row['Longitude']

#         temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
#         weather_advice = generate_weather_advice(city_name, temp, condition, lang="en", is_first_city=(index == 0))

#         # Download image
#         background_image = download_background_image(city_name, condition)

#         # Create map image
#         map_image = create_map(lat, lon, city_name)

#         # Create final image sequence and audio file
#         image_sequences.append([map_image, background_image])
        
#         audio_path = generate_audio(weather_advice, lang="en")
#         audio_paths.append(audio_path)

#     # Create video with the generated images and audio
#     create_video(image_sequences, audio_paths)

# # Example city data (replace with actual CSV or data)
# city_data = pd.DataFrame({
#     'Location': ['Hyderabad', 'Bangalore', 'Chennai'],
#     'Latitude': [17.385044, 12.971598, 13.082680],
#     'Longitude': [78.486671, 77.594566, 80.270718]
# })

# generate_weather_video(city_data)



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
#     if response.status_code == 200:
#         data = response.json()
#         return data['current']['temp_c'], data['current']['condition']['text']
#     return None, None

# # Generate AI-based weather advice
# def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
#     greeting = get_greeting() if is_first_city else ""
#     context = f"{city}: {temp}°C, {condition}."
    
#     prompt = f"""{context} 
#     Give a very short and clear weather suggestion in one sentence. 
#     Example: "Carry an umbrella if it rains." or "Wear warm clothes if it's cold."
#     """
#     response = chat_model.predict(prompt).strip()

#     if lang != "en":
#         response = GoogleTranslator(source="auto", target=lang).translate(response)
    
#     return f"{greeting} {context} {response}".strip()

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
#             return image_path

#     return "fallback.jpg"  # Use a fallback image if API fails

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
#     img = img.resize((1280, 720))
#     draw = ImageDraw.Draw(img)

#     try:
#         font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"  # Update this
#         font = ImageFont.truetype(font_path, 50)
#     except OSError:
#         print("⚠️ Font file not found, using default font.")
#         font = ImageFont.load_default()

#     text_position = (50, 50)
#     draw.text(text_position, text, fill="white", font=font)

#     output_path = f"overlay_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path


# # Generate audio from text
# def generate_audio(text, lang="en"):
#     tts = gTTS(text=text, lang=lang, slow=False)
#     audio_file = "weather_advice.mp3"
#     tts.save(audio_file)
#     return audio_file

# # Create video sequence
# def create_video(image_sequences, audio_paths, output_file="weather_report.mp4"):
#     final_clips = []
    
#     for images, audio in zip(image_sequences, audio_paths):
#         audio_clip = AudioFileClip(audio)
#         duration = audio_clip.duration

#         # Show map image for 2 seconds
#         map_clip = ImageSequenceClip([images[0]], durations=[2])

#         # Show background image for the remaining time
#         background_clip = ImageSequenceClip([images[1]], durations=[duration - 2])
        
#         # Crossfade transition
#         video_clip = concatenate_videoclips([map_clip, background_clip], method="compose").crossfadein(1)

#         video_clip = video_clip.set_audio(audio_clip)
        
#         final_clips.append(video_clip)
    
#     final_video = concatenate_videoclips(final_clips)
#     final_video.write_videofile(output_file, codec="libx264", fps=30, bitrate="5000k", preset="slow")

# # Main function to process cities and generate weather video
# def generate_weather_video(city_data):
#     image_sequences = []
#     audio_paths = []

#     for index, row in city_data.iterrows():
#         city_name = row['Location']
#         lat, lon = row['Latitude'], row['Longitude']

#         temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
#         weather_advice = generate_weather_advice(city_name, temp, condition, lang="en", is_first_city=(index == 0))

#         # Download background image
#         background_image = download_background_image(city_name, condition)
#         background_image = add_text_overlay(background_image, f"{city_name}: {temp}°C, {condition}")

#         # Create map image
#         map_image = create_map(lat, lon, city_name)

#         # Prepare image sequence and audio
#         image_sequences.append([map_image, background_image])
#         audio_path = generate_audio(weather_advice, lang="en")
#         audio_paths.append(audio_path)

#     # Generate final video
#     create_video(image_sequences, audio_paths)

# # Example city data
# city_data = pd.DataFrame({
#     'Location': ['Hyderabad', 'Bangalore', 'Chennai'],
#     'Latitude': [17.385044, 12.971598, 13.082680],
#     'Longitude': [78.486671, 77.594566, 80.270718]
# })

# generate_weather_video(city_data)


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
#         font_path = ""
    
#         if lang == "te":
#             font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Telugu font path
#         elif lang == "hi":
#             font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf"  # Hindi font path
#         elif lang == "kn":
#             font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Kannada/NotoSansKannada-VariableFont_wdth,wght.ttf"  # Kannada font path
#         elif lang == "ml":
#             font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Malayalam/NotoSansMalayalam-VariableFont_wdth,wght.ttf"  # Malayalam font path
#         elif lang == "ta":
#             font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Tamil/NotoSansTamil-VariableFont_wdth,wght.ttf"  # Tamil font path
#         else:
#             font_path = "/Users/nc25572_mourya/Downloads/Noto_Sans_Devanagari,Noto_Sans_Kannada,Noto_Sans_Malayalam,Noto_Sans_Tamil,Noto_Sans_Telugu/Noto_Sans_Telugu/NotoSansTelugu-VariableFont_wdth,wght.ttf"  # Default font path (e.g., for English)

#             font = ImageFont.truetype(font_path, 50)
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

# # Set Google credentials
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nc25572_mourya/Downloads/ttsaudio-449211-16297ceac279.json"
# translator_client = translate.Client()

# # API Keys (Replace with your own)
# WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
# UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"
# GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"

# # Initialize Google Gemini Chat model
# chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

# def fetch_unsplash_image(city, condition):
#     """Fetches a relevant background image from Unsplash based on city or weather condition."""
#     query = f"{city} {condition} weather"
#     url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}&orientation=landscape"

#     response = requests.get(url)
#     if response.status_code == 200:
#         image_url = response.json()["urls"]["regular"]
#         image_path = f"backgrounds/{city}.jpg"

#         os.makedirs("backgrounds", exist_ok=True)
#         img_data = requests.get(image_url).content
#         with open(image_path, "wb") as img_file:
#             img_file.write(img_data)

#         return resize_image(image_path)  # Resize and return path
#     else:
#         print(f"⚠️ Failed to fetch background for {city}, using fallback.")
#         return resize_image("fallback.jpg")




# def get_greeting():
#     """Returns a greeting based on the current time."""
#     hour = datetime.datetime.now().hour
#     return "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"


# from moviepy.editor import TextClip, CompositeVideoClip

# def create_scrolling_text(text, duration, video_size=(1280, 720), font_size=40, speed=150):
#     """Generates a scrolling text overlay video."""
#     text_clip = TextClip(text, fontsize=font_size, color='white', font="Arial-Bold")

#     text_width, text_height = text_clip.size
#     start_x = video_size[0]  # Start from the right
#     end_x = -text_width  # Move to the left
    
#     text_clip = text_clip.set_position(lambda t: (start_x - speed * t, video_size[1] - 100))  # Scroll at speed
#     text_clip = text_clip.set_duration(duration)  # Set duration

#     return text_clip


# def create_video_with_scrolling_text(image_sequences, audio_files, weather_texts, output_file="weather_report.mp4"):
#     """Creates a weather report video with map, background, and scrolling weather data."""
#     final_clips = []

#     for images, audio_file, weather_text in zip(image_sequences, audio_files, weather_texts):
#         audio_clip = AudioFileClip(audio_file)
#         duration = audio_clip.duration

#         # Zoom effect for map (first 2 seconds)
#         zoom_frames = []
#         map_image = Image.open(images[0])

#         for scale in np.linspace(1, 1.2, num=10):  
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
#         background_clip = ImageSequenceClip([images[1]], durations=[duration - 2]).crossfadein(1)

#         video_clip = concatenate_videoclips([map_clip, background_clip], method="compose")
#         video_clip = video_clip.set_audio(audio_clip)

#         # Add scrolling weather text overlay
#         scrolling_text_clip = create_scrolling_text(weather_text, duration)
#         video_with_text = CompositeVideoClip([video_clip, scrolling_text_clip])

#         final_clips.append(video_with_text)

#     final_video = concatenate_videoclips(final_clips, method="compose")
#     final_video.write_videofile(output_file, codec="libx264", fps=30, bitrate="5000k")
#     final_video.close()


# def generate_weather_video(city_data, lang="en"):
#     """Processes city weather data and generates a video with scrolling text."""
#     image_sequences = []
#     audio_paths = []
#     weather_texts = []

#     for index, row in city_data.iterrows():
#         city_name = row['Location']
#         lat, lon = row['Latitude'], row['Longitude']

#         temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
#         if temp is None or condition is None:
#             continue

#         display_text, audio_text = generate_weather_advice(city_name, temp, condition, lang, is_first_city=(index == 0))

#         map_image = create_map(lat, lon, city_name)
#         background_image = fetch_unsplash_image(city_name, condition)

#         image_sequences.append([map_image, background_image])
#         audio_path = generate_audio(audio_text, city_name, lang)
#         if audio_path:
#             audio_paths.append(audio_path)

#         weather_texts.append(display_text)  # Store scrolling text

#     create_video_with_scrolling_text(image_sequences, audio_paths, weather_texts)



# # Example city data
# # city_data = pd.DataFrame({
# #     'Location': ['Hyderabad', 'Bangalore', 'Chennai'],
# #     'Latitude': [17.385044, 12.971598, 13.082680],
# #     'Longitude': [78.486671, 77.594566, 80.270718]
# # })

# # generate_weather_video(city_data)

# def fetch_weather(api_key, lat, lon):
#     """Fetches weather details from Weather API with retry logic."""
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"
    
#     for attempt in range(3):  # Retry up to 3 times
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json().get('current', {})
#             return data.get('temp_c', None), data.get('condition', {}).get('text', "")
#         time.sleep(2)
    
#     print(f"⚠️ Weather API failed for {lat}, {lon}")
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


# def generate_weather_advice(city, temp, condition, lang="en", is_first_city=False):
#     """Generates AI-based weather advice."""
#     greeting = get_greeting() if is_first_city else ""
    
#     translated_city = translate_text_google(city, lang)
#     translated_condition = translate_text_google(condition, lang)
#     translated_temp = translate_text_google(f"The temperature is {temp}°C.", lang)

#     context = f"{city}: {temp}°C, {condition}."
#     prompt = f"""{context} 
#     Give a short and clear weather suggestion in one sentence."""

#     response = chat_model.predict(prompt).strip().replace("*", "")
#     translated_suggestion = translate_text_google(response, lang)

#     audio_text = f"{greeting} {translated_city}, {translated_temp}, {translated_condition}. {translated_suggestion}".strip()
#     display_text = f"{translated_city}: {temp}°C, {translated_condition}. {translated_suggestion}".strip()

#     return display_text, audio_text


# def resize_image(image_path, target_size=(1280, 720)):
#     """Resizes an image to the given target size."""
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize(target_size, Image.Resampling.LANCZOS)

#     output_path = f"resized_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path

def create_map(lat, lon, city_name):
    """Generates a dynamic map image with a marker for each city."""
    os.makedirs("maps", exist_ok=True)
    map_file = f"maps/{city_name}.html"

    # Create map
    folium_map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup=city_name).add_to(folium_map)
    folium_map.save(map_file)

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x720")

    driver = webdriver.Chrome(options=options)
    driver.get(f"file://{os.path.abspath(map_file)}")

    # Ensure the map fully loads before capturing
    time.sleep(3)  # Increase if needed
    
    # Force refresh and wait for rendering
    driver.execute_script("location.reload();")
    time.sleep(3)

    # Scroll to the correct position before capturing
    driver.execute_script("window.scrollTo(0, 0)")

    screenshot_path = f"maps/{city_name}.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()

    return resize_image(screenshot_path)



# def generate_audio(text, city_name, lang="en"):
#     """Generates an audio file from text using gTTS."""
#     try:
#         audio_file = f"weather_advice_{city_name}.mp3"
#         tts = gTTS(text=text, lang=lang, slow=False)
#         tts.save(audio_file)
#         return audio_file
#     except Exception as e:
#         print(f"⚠️ Audio generation failed: {e}")
#         return None

# def create_video(image_sequences, audio_files, output_file="weather_report.mp4"):
#     """Creates a weather report video with smooth transitions between clips."""
#     final_clips = []

#     for images, audio_file in zip(image_sequences, audio_files):
#         audio_clip = AudioFileClip(audio_file)
#         duration = audio_clip.duration

#         # Create a zoom effect for the map (first 2 seconds)
#         zoom_frames = []
#         map_image = Image.open(images[0])

#         for scale in np.linspace(1, 1.2, num=10):  # Zoom from 100% to 120%
#             width, height = map_image.size
#             new_width, new_height = int(width * scale), int(height * scale)
#             zoomed_img = map_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

#             # Crop to original size to avoid black edges
#             left = (new_width - width) // 2
#             top = (new_height - height) // 2
#             zoomed_img = zoomed_img.crop((left, top, left + width, top + height))

#             frame_path = f"temp_zoom_{scale:.2f}.jpg"
#             zoomed_img.save(frame_path)
#             zoom_frames.append(frame_path)

#         map_clip = ImageSequenceClip(zoom_frames, fps=10)  # Smooth zoom effect (2 seconds)
#         background_clip = ImageSequenceClip([images[1]], durations=[duration - 2])

#         # Apply crossfade transition (1 second)
#         map_clip = map_clip.set_duration(2).crossfadeout(1)
#         background_clip = background_clip.set_duration(duration - 2).crossfadein(1)

#         video_clip = concatenate_videoclips([map_clip, background_clip], method="compose")
#         video_clip = video_clip.set_audio(audio_clip)

#         final_clips.append(video_clip)

#     final_video = concatenate_videoclips(final_clips, method="compose")
#     final_video.write_videofile(output_file, codec="libx264", fps=30, bitrate="5000k")
#     final_video.close()


# # Example city data
# city_data = pd.DataFrame({
#     'Location': ['Hyderabad', 'Bangalore', 'Chennai'],
#     'Latitude': [17.385044, 12.971598, 13.082680],
#     'Longitude': [78.486671, 77.594566, 80.270718]
# })

# generate_weather_video(city_data)

# import os
# import time
# import datetime
# import requests
# import pandas as pd
# import numpy as np
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import (
#     ImageSequenceClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, TextClip
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

# def create_map(lat, lon, city_name):
#     """Generates a new map for each city dynamically."""
#     os.makedirs("maps", exist_ok=True)
#     map_file = f"maps/{city_name}.html"

#     folium_map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(folium_map)
#     folium_map.save(map_file)

#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1280x720")

#     driver = webdriver.Chrome(options=options)
#     driver.get(f"file://{os.path.abspath(map_file)}")

#     time.sleep(3)  # Allow map to fully render
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()

#     return resize_image(screenshot_path)

# def resize_image(image_path, target_size=(1280, 720)):
#     """Resizes an image to fit the target size."""
#     img = Image.open(image_path).convert("RGB")
#     img = img.resize(target_size, Image.Resampling.LANCZOS)

#     output_path = f"resized_{os.path.basename(image_path)}"
#     img.save(output_path)
#     return output_path

# def generate_audio(text, city_name, lang="en"):
#     """Generates an audio file from text using gTTS."""
#     try:
#         audio_file = f"weather_audio_{city_name}.mp3"
#         tts = gTTS(text=text, lang=lang, slow=False)
#         tts.save(audio_file)
#         return audio_file
#     except Exception as e:
#         print(f"⚠️ Audio generation failed: {e}")
#         return None

def create_scrolling_text(text, duration, video_size=(1280, 720), font_size=40, speed=150):
    """Generates a scrolling text overlay video."""
    text_clip = TextClip(text, fontsize=font_size, color='white', font="Arial-Bold")

    text_width, _ = text_clip.size
    start_x = video_size[0]
    
    text_clip = text_clip.set_position(lambda t: (start_x - speed * t, video_size[1] - 100))
    text_clip = text_clip.set_duration(duration)

    return text_clip

def create_video(image_sequences, audio_files, weather_texts, output_file="weather_report.mp4"):
    """Creates a weather report video for each city with new maps."""
    final_clips = []

    for images, audio_file, weather_text in zip(image_sequences, audio_files, weather_texts):
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration

        zoom_frames = []
        map_image = Image.open(images[0])

        for scale in np.linspace(1, 1.2, num=10):
            width, height = map_image.size
            new_width, new_height = int(width * scale), int(height * scale)
            zoomed_img = map_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

            left = (new_width - width) // 2
            top = (new_height - height) // 2
            zoomed_img = zoomed_img.crop((left, top, left + width, top + height))

            frame_path = f"temp_zoom_{scale:.2f}.jpg"
            zoomed_img.save(frame_path)
            zoom_frames.append(frame_path)

        map_clip = ImageSequenceClip(zoom_frames, fps=10).set_duration(2).crossfadeout(1)
        background_clip = ImageSequenceClip([images[1]], durations=[duration - 2]).crossfadein(1)

        video_clip = concatenate_videoclips([map_clip, background_clip], method="compose")
        video_clip = video_clip.set_audio(audio_clip)

        scrolling_text_clip = create_scrolling_text(weather_text, duration)
        video_with_text = CompositeVideoClip([video_clip, scrolling_text_clip])

        final_clips.append(video_with_text)

    final_video = concatenate_videoclips(final_clips, method="compose")
    final_video.write_videofile(output_file, codec="libx264", fps=30, bitrate="5000k")
    final_video.close()

# def generate_weather_video(city_data, lang="en"):
#     """Processes city weather data and generates a video with a new map for each city."""
#     image_sequences = []
#     audio_paths = []
#     weather_texts = []

#     for index, row in city_data.iterrows():
#         city_name = row['Location']
#         lat, lon = row['Latitude'], row['Longitude']

#         temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
#         if temp is None or condition is None:
#             continue

#         translated_city = city_name
#         translated_condition = condition
#         translated_temp = f"The temperature is {temp}°C."
#         greeting = "Good morning" if datetime.datetime.now().hour < 12 else "Good evening"

#         prompt = f"{city_name}: {temp}°C, {condition}. Provide a short weather suggestion."
#         response = chat_model.predict(prompt).strip().replace("*", "")
#         translated_suggestion = response

#         audio_text = f"{greeting} {translated_city}, {translated_temp}, {translated_condition}. {translated_suggestion}".strip()
#         display_text = f"{translated_city}: {temp}°C, {translated_condition}. {translated_suggestion}".strip()

#         map_image = create_map(lat, lon, city_name)

#         image_sequences.append([map_image])
#         audio_path = generate_audio(audio_text, city_name, lang)
#         if audio_path:
#             audio_paths.append(audio_path)

#         weather_texts.append(display_text)

#     create_video(image_sequences, audio_paths, weather_texts)

# # Example city data
# city_data = pd.DataFrame({
#     'Location': ['Hyderabad', 'Bangalore', 'Chennai'],
#     'Latitude': [17.385044, 12.971598, 13.082680],
#     'Longitude': [78.486671, 77.594566, 80.270718]
# })

# generate_weather_video(city_data)



import os
import time
import datetime
import requests
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from moviepy.editor import (
    ImageSequenceClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, TextClip
)
import folium
from selenium import webdriver
from deep_translator import GoogleTranslator
from pydub import AudioSegment
from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import translate_v2 as translate

# Set Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/nc25572_mourya/Downloads/ttsaudio-449211-16297ceac279.json"
translator_client = translate.Client()

# API Keys (Replace with your own)
WEATHER_API_KEY = "22cd9db3340944d697b173414252401"
UNSPLASH_ACCESS_KEY = "qBpzf5SOb4nveKq44bDIBnCzj4atEyxzsmpUUmqLVhU"
GEMINI_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"

# Initialize Google Gemini Chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, api_key=GEMINI_API_KEY)

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

def fetch_unsplash_image(city, condition):
    """Fetches a relevant background image from Unsplash based on weather conditions."""
    query = f"{city} {condition} weather"
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}&orientation=landscape"

    response = requests.get(url)
    if response.status_code == 200:
        image_url = response.json().get("urls", {}).get("regular")
        if image_url:
            image_path = f"backgrounds/{city}.jpg"
            os.makedirs("backgrounds", exist_ok=True)
            img_data = requests.get(image_url).content
            with open(image_path, "wb") as img_file:
                img_file.write(img_data)
            return resize_image(image_path)

    print(f"⚠️ Failed to fetch background for {city}, using fallback.")
    return resize_image("fallback.jpg")  # Ensure fallback image is always available

def create_map(lat, lon, city_name):
    """Generates a map for each city."""
    try:
        os.makedirs("maps", exist_ok=True)
        map_file = f"maps/{city_name}.html"

        folium_map = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], popup=city_name).add_to(folium_map)
        folium_map.save(map_file)

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1280x720")

        driver = webdriver.Chrome(options=options)
        driver.get(f"file://{os.path.abspath(map_file)}")

        time.sleep(3)  # Allow rendering
        screenshot_path = f"maps/{city_name}.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()

        return resize_image(screenshot_path)

    except Exception as e:
        print(f"⚠️ Failed to generate map for {city_name}, using default map.")
        return "default_map.png"

def resize_image(image_path, target_size=(1280, 720)):
    """Resizes an image to fit the target size."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize(target_size, Image.Resampling.LANCZOS)
    output_path = f"resized_{os.path.basename(image_path)}"
    img.save(output_path)
    return output_path

def generate_audio(text, city_name, lang="en"):
    """Generates an audio file from text using gTTS."""
    try:
        audio_file = f"weather_audio_{city_name}.mp3"
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(audio_file)
        return audio_file
    except Exception as e:
        print(f"⚠️ Audio generation failed: {e}")
        return None

def generate_weather_video(city_data, lang="en"):
    """Processes city weather data and generates a weather report video."""
    image_sequences = []
    audio_paths = []
    weather_texts = []

    for _, row in city_data.iterrows():
        city_name = row['Location']
        lat, lon = row['Latitude'], row['Longitude']

        temp, condition = fetch_weather(WEATHER_API_KEY, lat, lon)
        if temp is None or condition is None:
            continue

        greeting = "Good morning" if datetime.datetime.now().hour < 12 else "Good evening"

        prompt = f"{city_name}: {temp}°C, {condition}. Provide a short weather suggestion."
        response = chat_model.predict(prompt).strip().replace("*", "")

        audio_text = f"{greeting} {city_name}, the temperature is {temp}°C with {condition}. {response}"
        display_text = f"{city_name}: {temp}°C, {condition}. {response}"

        map_image = create_map(lat, lon, city_name)
        background_image = fetch_unsplash_image(city_name, condition)

        if map_image and background_image:
            image_sequences.append([map_image, background_image])
            audio_path = generate_audio(audio_text, city_name, lang)
            if audio_path:
                audio_paths.append(audio_path)
            weather_texts.append(display_text)
        else:
            print(f"⚠️ Skipping {city_name} due to missing images.")

    if image_sequences and audio_paths:
        create_video(image_sequences, audio_paths, weather_texts)

# Example city data
city_data = pd.DataFrame({
    'Location': ['Hyderabad', 'Bangalore', 'Chennai'],
    'Latitude': [17.385044, 12.971598, 13.082680],
    'Longitude': [78.486671, 77.594566, 80.270718]
})

generate_weather_video(city_data)
