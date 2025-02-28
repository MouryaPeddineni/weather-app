# import folium
# import time
# import os
# from selenium import webdriver
# from PIL import Image
# from moviepy.editor import ImageSequenceClip

# # Function to create map and save it as an image
# def create_map(lat, lon, city_name):
#     # Create map centered at the city's latitude and longitude
#     map = folium.Map(location=[lat, lon], zoom_start=12)
    
#     # Add a marker for the city
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     # Save the map as an HTML file
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)

#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Run in headless mode (no browser UI)
#     driver = webdriver.Chrome(options=options)

#     # Open the map HTML file in the browser
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load

#     # Take a screenshot of the map
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()

#     # Crop the screenshot to remove unwanted borders
#     img = Image.open(screenshot_path)
#     img = img.crop((0, 50, img.width, img.height - 100))  # Adjust as needed
#     img.save(screenshot_path)
    
    # return screenshot_path

# Function to create a video from a series of images (maps)
# def create_video(image_paths, output_video_path):
#     clip = ImageSequenceClip(image_paths, fps=1)  # 1 frame per second
#     clip.write_videofile(output_video_path, codec="libx264")

# # Main code for generating maps and creating a video
# def main():
#     # List of cities with their latitudes and longitudes
#     cities = [
#         {"name": "New York", "lat": 40.7128, "lon": -74.0060},
#         {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
#         {"name": "Chicago", "lat": 41.8781, "lon": -87.6298}
#     ]
    
#     if not os.path.exists('maps'):
#         os.makedirs('maps')

#     image_paths = []
#     for city in cities:
#         screenshot_path = create_map(city["lat"], city["lon"], city["name"])
#         image_paths.append(screenshot_path)

#     # Create a video from the generated map images
#     create_video(image_paths, "weather_map_animation.mp4")

#     print("Map animation video created successfully!")

# if __name__ == "__main__":
#     main()


# import folium
# import time
# import os
# from selenium import webdriver
# from PIL import Image, ImageDraw, ImageFont
# import requests
# from moviepy.editor import ImageSequenceClip

# # Function to fetch weather details from OpenWeatherMap API
# def get_weather_details(lat, lon):
#     api_key = "22cd9db3340944d697b173414252401"  # Replace with your OpenWeatherMap API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
    
#     if data.get("cod") == 200:
#         temperature = data["main"]["temp"]
#         weather_condition = data["weather"][0]["description"]
#         return f"{temperature}°C, {weather_condition}"
#     else:
#         return "Weather data unavailable"

# # Function to create map, save it as an image, and add weather details
# def create_map(lat, lon, city_name):
#     # Create map centered at the city's latitude and longitude
#     map = folium.Map(location=[lat, lon], zoom_start=12)
    
#     # Add a marker for the city
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     # Save the map as an HTML file
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)

#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Run in headless mode (no browser UI)
#     driver = webdriver.Chrome(options=options)

#     # Open the map HTML file in the browser
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load

#     # Take a screenshot of the map
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()

#     # Get the weather details for the location
#     weather_details = get_weather_details(lat, lon)

#     # Add weather details to the screenshot using PIL
#     img = Image.open(screenshot_path)
#     draw = ImageDraw.Draw(img)
    
#     # Choose a font and size for the weather details (adjust as needed)
#     font = ImageFont.load_default()
    
#     # Add weather text to the image (position, font size, color, etc. can be adjusted)
#     draw.text((10, img.height - 50), f"{city_name}: {weather_details}", font=font, fill="black")

#     # Save the image with weather details
#     img.save(screenshot_path)
    
#     return screenshot_path

# # Function to create a video from a series of images (maps)
# def create_video(image_paths, output_video_path):
#     clip = ImageSequenceClip(image_paths, fps=1)  # 1 frame per second
#     clip.write_videofile(output_video_path, codec="libx264")

# # Main code for generating maps and creating a video
# def main():
#     # List of cities with their latitudes and longitudes
#     cities = [
#         {"name": "New York", "lat": 40.7128, "lon": -74.0060},
#         {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
#         {"name": "Chicago", "lat": 41.8781, "lon": -87.6298}
#     ]
    
#     if not os.path.exists('maps'):
#         os.makedirs('maps')

#     image_paths = []
#     for city in cities:
#         screenshot_path = create_map(city["lat"], city["lon"], city["name"])
#         image_paths.append(screenshot_path)

#     # Create a video from the generated map images
#     create_video(image_paths, "weather_map_animation.mp4")

#     print("Map animation video created successfully!")

# if __name__ == "__main__":
#     main()




# import folium
# import time
# import os
# from selenium import webdriver
# from PIL import Image
# from moviepy.editor import ImageSequenceClip, CompositeVideoClip, ColorClip, ImageClip

# # Function to create map and save it as an image
# def create_map(lat, lon, city_name, zoom_start=5):
#     # Create map centered at the city's latitude and longitude
#     map = folium.Map(location=[lat, lon], zoom_start=zoom_start)
    
#     # Add a marker for the city
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     # Save the map as an HTML file
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)

#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Run in headless mode (no browser UI)
#     driver = webdriver.Chrome(options=options)

#     # Open the map HTML file in the browser
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load

#     # Take a screenshot of the map
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()

#     # Crop the screenshot to remove unwanted borders
#     img = Image.open(screenshot_path)
#     img = img.crop((0, 50, img.width, img.height - 100))  # Adjust as needed
#     img.save(screenshot_path)
    
#     return screenshot_path

# # Function to create a zoom-in effect on the city
# def create_zoom_in_effect(cities):
#     image_paths = []
#     # First, show the entire India map at a low zoom
#     india_map_image = create_map(20.5937, 78.9629, "India", zoom_start=4)  # India lat/lon
#     image_paths.append(india_map_image)
    
#     # Then zoom into each city
#     for city in cities:
#         city_image = create_map(city["lat"], city["lon"], city["name"], zoom_start=10)
#         image_paths.append(city_image)
    
#     return image_paths

# # Function to create a video from a series of images (maps)
# from moviepy.editor import ImageSequenceClip

# # Function to add fade-out effect to the last frame
# def add_fade_out_effect(image_path, duration=2, fps=24):
#     # Load the final image (city map)
#     final_image = Image.open(image_path)
#     final_image.save("temp_image.png")  # Save as temporary image to use in MoviePy

#     # Create an ImageClip from the final image
#     fade_clip = ImageClip("temp_image.png", duration=duration)  # Set duration here
    
#     # Apply fade-out effect (fade out to black)
#     fade_clip = fade_clip.fadeout(duration)
    
#     # Set the fps for the fade clip
#     fade_clip.fps = fps
    
#     return fade_clip

# # Function to create video from a series of images
# def create_video(image_paths, output_video_path, fps=24):
#     # Create a video clip from the sequence of images
#     clip = ImageSequenceClip(image_paths, fps=fps)  # Set fps here
#     clip.write_videofile(output_video_path, codec="libx264")



# # Main code for generating maps and creating a video
# def main():
#     # List of cities with their latitudes and longitudes
#     cities = [
#         {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777},
#         {"name": "Delhi", "lat": 28.6139, "lon": 77.2090},
#         {"name": "Bangalore", "lat": 12.9716, "lon": 77.5946}
#     ]
    
#     if not os.path.exists('maps'):
#         os.makedirs('maps')

#     # Generate zoomed-in images for each city
#     image_paths = create_zoom_in_effect(cities)
    
#     # Apply fade-out effect to the last image
#     fade_out_video = add_fade_out_effect(image_paths[-1])

#     # Create a video from the generated map images
#     create_video(image_paths[:-1], "weather_map_zoom.mp4")
#     fade_out_video.write_videofile("weather_map_zoom_with_fade_out.mp4", codec="libx264")

#     print("Map animation video with fade-out effect created successfully!")

# if __name__ == "__main__":
#     main()


# import os
# from PIL import Image, ImageDraw
# from moviepy.editor import ImageSequenceClip, concatenate_videoclips, VideoFileClip
# import numpy as np

# # Function to crop the map of India and focus on a specific region (city)
# def crop_map(map_path, city_coords, zoom_level=5):
#     # Load the map image
#     india_map = Image.open(map_path)
    
#     # Coordinates of India (in the original map's scale)
#     # Modify these values to fit your specific map dimensions
#     india_box = (50, 50, 600, 800)  # Example: (left, top, right, bottom)
    
#     # Crop to focus on India
#     india_cropped = india_map.crop(india_box)
    
#     # Pin the city (city_coords is a tuple (lat, long))
#     pin_color = (255, 0, 0)  # Red
#     city_x, city_y = city_coords  # Example city coordinates on the cropped map
#     draw = ImageDraw.Draw(india_cropped)
#     draw.ellipse((city_x-10, city_y-10, city_x+10, city_y+10), fill=pin_color)  # Drawing pin
    
#     # Apply zoom effect (this will need to be adjusted based on the city and zoom level)
#     width, height = india_cropped.size
#     new_width = int(width * zoom_level)
#     new_height = int(height * zoom_level)
    
#     # Zoom into the city by cropping and resizing
#     zoomed_map = india_cropped.crop((city_x - new_width // 2, city_y - new_height // 2, 
#                                      city_x + new_width // 2, city_y + new_height // 2))
#     zoomed_map = zoomed_map.resize((width, height))  # Resize to original size
    
#     return india_cropped, zoomed_map

# # Function to create the zoom-in effect for the city
# def create_zoom_video(initial_map, zoomed_map, output_path, fps=24, duration=4):
#     # Convert the images to video clips
#     initial_clip = ImageSequenceClip([initial_map], fps=fps)
#     zoomed_clip = ImageSequenceClip([zoomed_map], fps=fps)
    
#     # Concatenate the initial and zoomed clips
#     final_clip = concatenate_videoclips([initial_clip, zoomed_clip])
    
#     # Write the final video file
#     final_clip.write_videofile(output_path, codec="libx264")
    
#     return final_clip

# # Main function to generate the map animation video
# def main():
#     map_path = "/Users/nc25572_mourya/Desktop/india_map.jpg"  # Replace with the path to your map of India
#     city_coords = (300, 400)  # Replace with the actual coordinates of the city in the map

#     # Create the cropped and zoomed map images
#     initial_map, zoomed_map = crop_map(map_path, city_coords)

#     # Save the cropped map images
#     initial_map.save("cropped_map.png")
#     zoomed_map.save("zoomed_map.png")

#     # Create the zoom video
#     output_path = "weather_map_zoom.mp4"
#     create_zoom_video("cropped_map.png", "zoomed_map.png", output_path)

# if __name__ == "__main__":
#     main()


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from geopy.geocoders import Nominatim
# from PIL import Image
# from moviepy.editor import ImageSequenceClip, concatenate_videoclips
# import time
# import os

# # Function to get city coordinates
# def get_city_coordinates(city_name):
#     return 19.0760, 72.8777


# # Function to generate map using Folium and take a screenshot with Selenium
# def generate_map(city_name, zoom_level, file_name):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         print(f"Could not find coordinates for {city_name}.")
#         return None
    
#     # Create Folium map
#     map_obj = folium.Map(location=coords, zoom_start=zoom_level, tiles="OpenStreetMap")

#     # Add a marker for the city
#     folium.Marker(location=coords, popup=city_name, icon=folium.Icon(color="red")).add_to(map_obj)

#     # Save map to an HTML file
#     map_html = "map.html"
#     map_obj.save(map_html)

#     # Capture screenshot using Selenium
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=800x600")
    
#     driver = webdriver.Chrome(options=options)
#     driver.get(f"file://{os.path.abspath(map_html)}")
    
#     time.sleep(2)  # Allow time for rendering
    
#     driver.save_screenshot(file_name)
#     driver.quit()

#     return file_name

# # Function to create zoom effect video
# def create_zoom_video(image1, image2, output_path, fps=24, duration=4):
#     initial_clip = ImageSequenceClip([image1], fps=fps)
#     zoomed_clip = ImageSequenceClip([image2], fps=fps)
    
#     final_clip = concatenate_videoclips([initial_clip, zoomed_clip])
#     final_clip.write_videofile(output_path, codec="libx264")
    
#     return output_path

# # Main function
# def main():
#     city_name = "Mumbai"  # Change this to the city of interest
    
#     # Generate India-level map
#     india_map = generate_map(city_name, zoom_level=5, file_name="india_map.png")
    
#     # Generate city-level zoomed map
#     city_map = generate_map(city_name, zoom_level=12, file_name="city_zoomed_map.png")
    
#     if india_map and city_map:
#         # Create zoom animation video
#         output_video = "weather_map_zoom.mp4"
#         create_zoom_video("india_map.png", "city_zoomed_map.png", output_video)
#         print(f"Video saved as {output_video}")
#     else:
#         print("Failed to generate maps.")

# if __name__ == "__main__":
#     main()


# import folium
# import time
# import os
# from selenium import webdriver
# from PIL import Image, ImageDraw, ImageFont
# import requests
# from moviepy.editor import ImageSequenceClip

# # Function to fetch weather details from OpenWeatherMap API
# def get_weather_details(lat, lon):
#     api_key = "22cd9db3340944d697b173414252401"  # Replace with your OpenWeatherMap API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
    
#     if data.get("cod") == 200:
#         temperature = data["main"]["temp"]
#         weather_condition = data["weather"][0]["description"]
#         return f"{temperature}°C, {weather_condition}"
#     return "20°C, 25°C"
#     # else:
#     #     return "Weather data unavailable"

# # Function to create map, save it as an image, and add weather details
# def create_map(lat, lon, city_name):
#     # Create map centered at the city's latitude and longitude
#     map = folium.Map(location=[lat, lon], zoom_start=12)
    
#     # Add a marker for the city
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     # Save the map as an HTML file
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)

#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Run in headless mode (no browser UI)
#     driver = webdriver.Chrome(options=options)

#     # Open the map HTML file in the browser
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load

#     # Take a screenshot of the map
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()

#     # Get the weather details for the location
#     weather_details = get_weather_details(lat, lon)

#     # Add weather details to the screenshot using PIL
#     img = Image.open(screenshot_path)
#     draw = ImageDraw.Draw(img)
    
#     # Choose a font and size for the weather details (adjust as needed)
#     font = ImageFont.load_default()  # Default font may not scale well, adjust if needed
    
#     # Print the weather details to console to ensure correct data
#     print(f"Weather for {city_name}: {weather_details}")

#     # Add weather text to the image (position, font size, color, etc. can be adjusted)
#     draw.text((10, img.height - 50), f"{city_name}: {weather_details}", font=font, fill="black")

#     # Save the image with weather details
#     img.save(screenshot_path)
    
#     return screenshot_path

# # Function to create a video from a series of images (maps)
# def create_video(image_paths, output_video_path):
#     clip = ImageSequenceClip(image_paths, fps=1)  # 1 frame per second
#     clip.write_videofile(output_video_path, codec="libx264")

# # Main code for generating maps and creating a video
# def main():
#     # List of cities with their latitudes and longitudes
#     cities = [
#         {"name": "New York", "lat": 40.7128, "lon": -74.0060},
#         {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
#         {"name": "Chicago", "lat": 41.8781, "lon": -87.6298}
#     ]
    
#     if not os.path.exists('maps'):
#         os.makedirs('maps')

#     image_paths = []
#     for city in cities:
#         screenshot_path = create_map(city["lat"], city["lon"], city["name"])
#         image_paths.append(screenshot_path)

#     # Create a video from the generated map images
#     create_video(image_paths, "weather_map_animation.mp4")

#     print("Map animation video created successfully!")

# if __name__ == "__main__":
#     main()


# import folium
# import time
# import os
# from selenium import webdriver
# from PIL import Image, ImageDraw, ImageFont
# import requests
# from moviepy.editor import ImageSequenceClip

# # Function to fetch weather details from OpenWeatherMap API
# def get_weather_details(lat, lon):
#     api_key = "22cd9db3340944d697b173414252401"  # Replace with your OpenWeatherMap API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
    
#     if data.get("cod") == 200:
#         temperature = data["main"]["temp"]
#         weather_condition = data["weather"][0]["description"]
#         return f"{temperature}°C, {weather_condition}"
#     else:
#         return "Weather data unavailable"

# # Function to create map, save it as an image, and add weather details
# def create_map(lat, lon, city_name):
#     # Create map centered at the city's latitude and longitude
#     map = folium.Map(location=[lat, lon], zoom_start=12)
    
#     # Add a marker for the city
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     # Save the map as an HTML file
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)

#     # Set up selenium to capture a screenshot of the map
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Run in headless mode (no browser UI)
#     driver = webdriver.Chrome(options=options)

#     # Open the map HTML file in the browser
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the map to load

#     # Take a screenshot of the map
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()

#     # Get the weather details for the location
#     weather_details = get_weather_details(lat, lon)

#     print(weather_details)

#     # Add weather details to the screenshot using PIL
#     img = Image.open(screenshot_path)
#     draw = ImageDraw.Draw(img)
    
#     try:
#         # Load a font (use any valid TTF font file path, you can download a font or use a system font)
#         font = ImageFont.truetype("arial.ttf", 20)
#     except IOError:
#         font = ImageFont.load_default()  # Fallback if custom font loading fails
    
#     # Print the weather details to console to ensure correct data
#     print(f"Weather for {city_name}: {weather_details}")

#     # Add weather text to the image (adjust position, font size, color, etc.)
#     text = f"{city_name}: {weather_details}"
#     text_position = (10, img.height - 60)  # Position the text 60 pixels from the bottom
#     draw.text(text_position, text, font=font, fill="white")

#     # Save the image with weather details
#     img.save(screenshot_path)
    
#     return screenshot_path

# # Function to create a video from a series of images (maps)
# def create_video(image_paths, output_video_path):
#     clip = ImageSequenceClip(image_paths, fps=1)  # 1 frame per second
#     clip.write_videofile(output_video_path, codec="libx264")

# # Main code for generating maps and creating a video
# def main():
#     # List of cities with their latitudes and longitudes
#     cities = [
#         {"name": "New York", "lat": 40.7128, "lon": -74.0060},
#         {"name": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
#         {"name": "Chicago", "lat": 41.8781, "lon": -87.6298}
#     ]
    
#     if not os.path.exists('maps'):
#         os.makedirs('maps')

#     image_paths = []
#     for city in cities:
#         screenshot_path = create_map(city["lat"], city["lon"], city["name"])
#         image_paths.append(screenshot_path)

#     # Create a video from the generated map images
#     create_video(image_paths, "weather_map_animation.mp4")

#     print("Map animation video created successfully!")

# if __name__ == "__main__":
#     main()


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
#             # Ensure the required weather data is available
#             if 'main' in weather_data and 'weather' in weather_data:
#                 temp = weather_data['main']['temp']
#                 condition = weather_data['weather'][0]['description'].title()
                
#                 # Generate image with map and weather details
#                 image_path = generate_image_with_map(location, temp, condition, lat, lon, index)
                
#                 # Generate audio for the weather report
#                 audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#                 audio_path = generate_audio(audio_text, index)
                
#                 image_paths.append(image_path)
#                 audio_paths.append(audio_path)
#             else:
#                 print(f"Missing weather data for {location}. Skipping this location.")
#         else:
#             print(f"Failed to fetch weather data for {location}. Skipping this location.")
    
#     # Create a video from the generated images and audio
#     create_video(image_paths, audio_paths)
    
#     # Cleanup temporary files
#     for file in image_paths + audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"  # Replace with your actual CSV file
#     api_key = "9032df887a070c6d2773ddfdfd431d7c"  # Replace with your API key
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
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips, concatenate_videoclips
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
# from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

# def create_video(images, output_path="output.mp4", fps=1):
#     # Debugging: Print the images list
#     print("Images List:", images)
    
#     # Ensure images list is not empty
#     if not images:
#         raise ValueError("Error: No images provided for video generation.")
    
#     # Convert to absolute paths and check if they exist
#     valid_images = [os.path.abspath(img) for img in images if os.path.exists(img)]
    
#     # Ensure valid images are available
#     if not valid_images:
#         raise FileNotFoundError("Error: No valid images found to create video.")

#     # Debugging: Print the final list of images to be used
#     print("Valid Images:", valid_images)

#     # Create the video
#     try:
#         map_clip = ImageSequenceClip(valid_images, fps=fps)  # Removed durations argument
#         map_clip.write_videofile(output_path, fps=fps)
#         print(f"Video successfully created: {output_path}")
#     except Exception as e:
#         print(f"Error during video creation: {e}")


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
# import requests
# import pandas as pd
# from PIL import Image, ImageDraw, ImageFont
# from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

# def fetch_weather_data(location, api_key):
#     url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Failed to fetch weather data for {location}: {response.text}")
#         return None

# def create_weather_image(weather_data, output_path):
#     width, height = 800, 600
#     image = Image.new('RGB', (width, height), (255, 255, 255))
#     draw = ImageDraw.Draw(image)
#     font = ImageFont.load_default()
    
#     location = weather_data['location']['name']
#     temp = weather_data['current']['temp_c']
#     condition = weather_data['current']['condition']['text']
    
#     text = f"Location: {location}\nTemperature: {temp}°C\nCondition: {condition}"
#     draw.text((50, 50), text, fill=(0, 0, 0), font=font)
    
#     image.save(output_path)

# def create_video_from_images(image_folder, output_video):
#     images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png")])
#     valid_images = [os.path.join(image_folder, img) for img in images]
    
#     if not valid_images:
#         print("No valid images found for video creation.")
#         return
    
#     clip = ImageSequenceClip(valid_images, fps=1)
#     clip.write_videofile(output_video, codec='libx264', fps=1)

# def main():
#     api_key = "22cd9db3340944d697b173414252401"
#     csv_path = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"  # Ensure this file exists with 'location' column
#     image_folder = "weather_images"
#     video_output = "weather_report.mp4"
    
#     if not os.path.exists(image_folder):
#         os.makedirs(image_folder)
    
#     df = pd.read_csv(csv_path)
    
#     for index, row in df.iterrows():
#         location = row['location']
#         weather_data = fetch_weather_data(location, api_key)
#         if weather_data:
#             image_path = os.path.join(image_folder, f"frame_{index}.png")
#             create_weather_image(weather_data, image_path)
    
#     create_video_from_images(image_folder, video_output)
#     print(f"Video saved at {video_output}")

# if __name__ == "__main__":
#     main()


# import os
# import pandas as pd
# import requests
# from PIL import Image, ImageDraw, ImageFont
# from gtts import gTTS
# from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_audioclips, CompositeVideoClip
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

# # Function to create a map and save it as an image
# def create_map(lat, lon, city_name):
#     map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker([lat, lon], popup=city_name).add_to(map)
    
#     map_file = f"maps/{city_name}.html"
#     map.save(map_file)
    
#     # Selenium setup for screenshot
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
    
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)
    
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     return screenshot_path

# # Function to generate an image with weather details
# def generate_image_with_map(location, temperature, condition, lat, lon, index):
#     map_image = create_map(lat, lon, location)
#     img = Image.open(map_image)
#     draw = ImageDraw.Draw(img)
    
#     font = ImageFont.load_default()
#     text = f"Weather Report for {location}\nTemperature: {temperature}°C\nCondition: {condition}"
    
#     draw.text((50, 300), text, fill='black', font=font)
    
#     img_path = f"frame_{index}.png"
#     img.save(img_path)
#     return img_path

# # Function to generate audio from text
# def generate_audio(text, index):
#     tts = gTTS(text=text, lang='en')
#     audio_path = f"audio_{index}.mp3"
#     tts.save(audio_path)
#     return audio_path

# # Function to create the video
# def create_video(images, audio_files, output_path="output.mp4", fps=1):
#     if not images:
#         raise ValueError("No images provided for video generation.")
    
#     valid_images = [os.path.abspath(img) for img in images if os.path.exists(img)]
#     if not valid_images:
#         raise FileNotFoundError("No valid images found to create video.")
    
#     # Create video from images
#     video_clip = ImageSequenceClip(valid_images, fps=fps)
    
#     # Merge audio files
#     audio_clips = [AudioFileClip(audio) for audio in audio_files if os.path.exists(audio)]
#     if audio_clips:
#         final_audio = concatenate_audioclips(audio_clips)
#         video_clip = video_clip.set_audio(final_audio)

#     video_clip.write_videofile(output_path, fps=fps)
#     print(f"Video successfully created: {output_path}")

# # Main function
# def main(csv_file, api_key):
#     df = pd.read_csv(csv_file)

#     if not {'location', 'latitude', 'longitude'}.issubset(df.columns):
#         print("CSV file must contain 'location', 'latitude', 'longitude'")
#         return

#     df = df.dropna(subset=['location', 'latitude', 'longitude'])
    
#     image_paths, audio_paths = [], []

#     for index, row in df.iterrows():
#         location, lat, lon = row['location'], row['latitude'], row['longitude']
#         weather_data = fetch_weather(api_key, lat, lon)
        
#         if weather_data and 'current' in weather_data:
#             temp = weather_data['current']['temp_c']
#             condition = weather_data['current']['condition']['text']
            
#             img_path = generate_image_with_map(location, temp, condition, lat, lon, index)
#             audio_text = f"The weather in {location} is {condition} with a temperature of {temp} degrees Celsius."
#             audio_path = generate_audio(audio_text, index)
            
#             image_paths.append(img_path)
#             audio_paths.append(audio_path)

#     create_video(image_paths, audio_paths)

#     for file in image_paths + audio_paths:
#         os.remove(file)

# if __name__ == "__main__":
#     csv_file = "/Users/nc25572_mourya/Desktop/untitled folder/uploaded_data.csv"
#     api_key = "22cd9db3340944d697b173414252401"
#     main(csv_file, api_key)

