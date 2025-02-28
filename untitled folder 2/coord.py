# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from geopy.geocoders import Nominatim

# # Function to get city coordinates using geopy
# def get_city_coordinates(city_name):
#     geolocator = Nominatim(user_agent="weather_map_app")  # Use a descriptive user agent
#     try:
#         location = geolocator.geocode(city_name)
#         if location:
#             return location.latitude, location.longitude
#         else:
#             print(f"Could not find coordinates for {city_name}.")
#             return None
#     except Exception as e:
#         print(f"Error occurred: {e}")
#         return None


# # Function to generate map using Folium and take a screenshot with Selenium
# def generate_map(city_name, zoom_level, file_name):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         print(f"Could not find coordinates for {city_name}.")
#         return None
    
#     # Create Folium map with fetched coordinates
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

# # Example usage:
# city_name = "Mumbai"
# generate_map(city_name, zoom_level=5, file_name="mumbai_map.png")


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your OpenCage API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         # Return the first result's latitude and longitude
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate map using Folium and take a screenshot with Selenium
# def generate_map(city_name, zoom_level, file_name):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         print(f"Could not find coordinates for {city_name}.")
#         return None
    
#     # Create Folium map with fetched coordinates
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

# # Example usage:
# city_name = "Mumbai"
# generate_map(city_name, zoom_level=5, file_name="mumbai_map.png")


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your OpenCage API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         # Return the first result's latitude and longitude
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate map using Folium and take a screenshot with Selenium
# def generate_map(city_name, zoom_level, file_name):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         print(f"Could not find coordinates for {city_name}.")
#         return None
    
#     # Create the map with an initial broader view of India
#     initial_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5, tiles="OpenStreetMap")  # India center

#     # Add a marker for the city (Mumbai)
#     folium.Marker(location=coords, popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#     # Set an initial timeout and fly_to method to zoom into the city (Mumbai)
#     folium.Marker(location=coords, popup=city_name).add_to(initial_map)

#     # Save map to an HTML file
#     map_html = "map.html"
#     initial_map.save(map_html)

#     # Capture screenshot using Selenium with zoom animation
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=800x600")

#     driver = webdriver.Chrome(options=options)
#     driver.get(f"file://{os.path.abspath(map_html)}")

#     time.sleep(2)  # Allow time for rendering

#     # Wait for a few seconds to give the zoom animation time to complete
#     time.sleep(3)

#     # Save the screenshot
#     driver.save_screenshot(file_name)
#     driver.quit()

#     return file_name

# # Example usage:
# city_name = "Mumbai"
# generate_map(city_name, zoom_level=5, file_name="mumbai_map_with_zoom.png")


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode
# from moviepy.editor import ImageSequenceClip

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your OpenCage API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         # Return the first result's latitude and longitude
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate map and save screenshots at different zoom levels
# def generate_map(city_name, zoom_level, file_name_prefix):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         print(f"Could not find coordinates for {city_name}.")
#         return None
    
#     # Create the map with an initial broader view of India
#     initial_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5, tiles="OpenStreetMap")  # India center

#     # Add a marker for the city (Mumbai)
#     folium.Marker(location=coords, popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#     # Save map at different zoom levels
#     screenshots = []
#     zoom_steps = range(5, 13)  # Zoom in from level 5 to 12
    
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=800x600")

#     driver = webdriver.Chrome(options=options)
    
#     for zoom in zoom_steps:
#         initial_map = folium.Map(location=[20.5937, 78.9629], zoom_start=zoom, tiles="OpenStreetMap")  # India center
#         folium.Marker(location=coords, popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#         # Save the map to an HTML file
#         map_html = "map.html"
#         initial_map.save(map_html)

#         # Open map in the browser using Selenium
#         driver.get(f"file://{os.path.abspath(map_html)}")
#         time.sleep(1)  # Allow time for rendering

#         # Save screenshot with the current zoom level
#         screenshot_path = f"{file_name_prefix}_zoom_{zoom}.png"
#         driver.save_screenshot(screenshot_path)
#         screenshots.append(screenshot_path)
    
#     driver.quit()
#     return screenshots

# # Function to create a video from screenshots
# def create_zoom_video(screenshots, output_video_file):
#     # Create a video clip from the screenshots
#     clip = ImageSequenceClip(screenshots, fps=2)  # Adjust fps for desired video speed
#     clip.write_videofile(output_video_file, codec="libx264")

# # Example usage:
# city_name = "Mumbai"
# screenshots = generate_map(city_name, zoom_level=5, file_name_prefix="zoom_mumbai")
# if screenshots:
#     create_zoom_video(screenshots, "zoom_mumbai_video.mp4")


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode
# from moviepy.editor import ImageSequenceClip

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your OpenCage API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         # Return the first result's latitude and longitude
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate map and save screenshots at different zoom levels
# def generate_map(city_name, zoom_level, file_name_prefix):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         print(f"Could not find coordinates for {city_name}.")
#         return None
    
#     # Save map at different zoom levels
#     screenshots = []
#     zoom_steps = [zoom_level + i * 0.5 for i in range(20)]  # Generate zoom levels from initial zoom level to zoom in slowly

#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=800x600")

#     driver = webdriver.Chrome(options=options)
    
#     for zoom in zoom_steps:
#         # Create the map with a centered view on the city (Mumbai)
#         initial_map = folium.Map(location=coords, zoom_start=zoom, tiles="OpenStreetMap")

#         # Add a marker for the city (Mumbai)
#         folium.Marker(location=coords, popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#         # Save the map to an HTML file
#         map_html = "map.html"
#         initial_map.save(map_html)

#         # Open map in the browser using Selenium
#         driver.get(f"file://{os.path.abspath(map_html)}")
#         time.sleep(1)  # Allow time for rendering

#         # Save screenshot with the current zoom level
#         screenshot_path = f"{file_name_prefix}_zoom_{int(zoom * 10)}.png"  # Use zoom level in filename
#         driver.save_screenshot(screenshot_path)
#         screenshots.append(screenshot_path)

#     driver.quit()
#     return screenshots

# # Function to create a video from screenshots
# def create_zoom_video(screenshots, output_video_file):
#     # Create a video clip from the screenshots
#     clip = ImageSequenceClip(screenshots, fps=24)  # Higher fps for smoother transition (e.g., 8 frames per second for 3-4 seconds)
#     clip.write_videofile(output_video_file, codec="libx264")

# # Example usage:
# city_name = "Mumbai"
# screenshots = generate_map(city_name, zoom_level=5, file_name_prefix="zoom_mumbai")
# if screenshots:
#     create_zoom_video(screenshots, "zoom_mumbai_video.mp4")


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode
# from moviepy.editor import ImageSequenceClip

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your OpenCage API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         # Return the first result's latitude and longitude
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate map and save screenshots at different zoom levels
# def generate_map(city_name, zoom_level, file_name_prefix):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         print(f"Could not find coordinates for {city_name}.")
#         return None
    
#     # Increase the number of zoom levels for smoother zoom (zoom in 0.1 increments)
#     screenshots = []
#     zoom_steps = [zoom_level + i * 0.1 for i in range(50)]  # Generate 50 zoom levels (more frames)

#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=800x600")

#     driver = webdriver.Chrome(options=options)
    
#     for zoom in zoom_steps:
#         # Create the map with a centered view on the city (Mumbai)
#         initial_map = folium.Map(location=coords, zoom_start=zoom, tiles="OpenStreetMap")

#         # Add a marker for the city (Mumbai)
#         folium.Marker(location=coords, popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#         # Save the map to an HTML file
#         map_html = "map.html"
#         initial_map.save(map_html)

#         # Open map in the browser using Selenium
#         driver.get(f"file://{os.path.abspath(map_html)}")
#         time.sleep(1)  # Allow time for rendering

#         # Save screenshot with the current zoom level
#         screenshot_path = f"{file_name_prefix}_zoom_{int(zoom * 10)}.png"  # Use zoom level in filename
#         driver.save_screenshot(screenshot_path)
#         screenshots.append(screenshot_path)
    
#     driver.quit()
#     return screenshots

# # Function to create a video from screenshots
# def create_zoom_video(screenshots, output_video_file):
#     # Create a video clip from the screenshots
#     clip = ImageSequenceClip(screenshots, fps=18)  # Set FPS to 12 for a slower, smoother animation
#     clip.write_videofile(output_video_file, codec="libx264")

# # Example usage:
# city_name = "Mumbai"
# screenshots = generate_map(city_name, zoom_level=5, file_name_prefix="zoom_mumbai")
# if screenshots:
#     create_zoom_video(screenshots, "zoom_mumbai_video.mp4")


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode
# from moviepy.editor import ImageSequenceClip

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your OpenCage API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate zoom effect map images
# def generate_map(city_name, zoom_level, file_name_prefix):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         return None
    
#     screenshots = []
#     zoom_steps = [zoom_level + i * 0.03 for i in range(100)]  # Smaller zoom increments for smoother zoom

#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=800x600")

#     driver = webdriver.Chrome(options=options)
    
#     for zoom in zoom_steps:
#         initial_map = folium.Map(location=coords, zoom_start=zoom, tiles="OpenStreetMap")
#         folium.Marker(location=coords, popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#         map_html = "map.html"
#         initial_map.save(map_html)

#         driver.get(f"file://{os.path.abspath(map_html)}")
#         time.sleep(0.5)  # Reduced delay for better efficiency

#         screenshot_path = f"{file_name_prefix}_zoom_{int(zoom * 100)}.png"
#         driver.save_screenshot(screenshot_path)
#         screenshots.append(screenshot_path)
    
#     driver.quit()
#     return screenshots

# # Function to create a smooth video
# def create_zoom_video(screenshots, output_video_file):
#     clip = ImageSequenceClip(screenshots, fps=12)  # Increased FPS for smooth animation
#     clip = clip.resize(height=720)  # Resize to 720p for better quality
#     clip.write_videofile(output_video_file, codec="libx264", preset="slow")

# # Example usage:
# city_name = "Mumbai"
# screenshots = generate_map(city_name, zoom_level=5, file_name_prefix="zoom_mumbai")
# if screenshots:
#     create_zoom_video(screenshots, "zoom_mumbai_video.mp4")



# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode
# from moviepy.editor import ImageSequenceClip

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate zoom-in effect with slight movement
# def generate_map(city_name, zoom_level, file_name_prefix):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         return None
    
#     screenshots = []
#     zoom_steps = [zoom_level * (1 + 0.01 * i) for i in range(200)]

#     lat_shift = 0.0002  # Small shift for panning effect
#     lng_shift = 0.0002  

#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=1200x800")  # Higher resolution

#     options.add_argument("--start-maximized")
#     options.add_argument("--enable-webgl")
#     options.add_argument("--disable-software-rasterizer")


#     driver = webdriver.Chrome(options=options)
    
#     for i, zoom in enumerate(zoom_steps):
#         lat = coords[0] + (i * lat_shift)
#         lng = coords[1] + (i * lng_shift)

#         initial_map = folium.Map(location=[lat, lng], zoom_start=zoom, tiles="OpenStreetMap")
#         folium.Marker(location=[lat, lng], popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#         map_html = "map.html"
#         initial_map.save(map_html)

#         driver.get(f"file://{os.path.abspath(map_html)}")
#         time.sleep(0.05)  # Lower sleep for faster rendering

#         screenshot_path = f"{file_name_prefix}_zoom_{i}.png"
#         driver.save_screenshot(screenshot_path)
#         screenshots.append(screenshot_path)
    
#     driver.quit()
#     return screenshots

# # Function to create a smooth zoom-in video
# def create_zoom_video(screenshots, output_video_file):
#     clip = ImageSequenceClip(screenshots, fps=45)  # Higher FPS for smooth animation
#     clip = clip.resize(height=1080)  # Upgrade to 1080p
#     clip.write_videofile(output_video_file, codec="libx264", preset="slow")

# # Example usage:
# city_name = "Mumbai"
# screenshots = generate_map(city_name, zoom_level=5, file_name_prefix="zoom_mumbai")
# if screenshots:
#     create_zoom_video(screenshots, "zoom_mumbai_video.mp4")


# import folium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time
# from opencage.geocoder import OpenCageGeocode
# from moviepy.editor import ImageSequenceClip

# # Function to get city coordinates using OpenCage API
# def get_city_coordinates(city_name):
#     key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your API key
#     geocoder = OpenCageGeocode(key)
#     result = geocoder.geocode(city_name)

#     if result:
#         lat = result[0]['geometry']['lat']
#         lon = result[0]['geometry']['lng']
#         return lat, lon
#     else:
#         print(f"Could not find coordinates for {city_name}.")
#         return None

# # Function to generate zoom-in effect with slight movement
# def generate_map(city_name, zoom_level, file_name_prefix):
#     coords = get_city_coordinates(city_name)
#     if not coords:
#         return None
    
#     screenshots = []
#     zoom_steps = [zoom_level * (1 + 0.01 * i) for i in range(200)]  # Exponential zoom

#     lat_shift = 0.0001  # Smaller shift for natural movement
#     lng_shift = 0.0001  

#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("window-size=1920x1080")  # Full HD
#     options.add_argument("--start-maximized")
#     options.add_argument("--enable-webgl")
#     options.add_argument("--disable-software-rasterizer")

#     driver = webdriver.Chrome(options=options)
    
#     for i, zoom in enumerate(zoom_steps):
#         lat = coords[0] + (i * lat_shift)
#         lng = coords[1] + (i * lng_shift)

#         initial_map = folium.Map(location=[lat, lng], zoom_start=zoom, tiles="OpenStreetMap")
#         folium.Marker(location=[lat, lng], popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

#         map_html = "map.html"
#         initial_map.save(map_html)

#         driver.get(f"file://{os.path.abspath(map_html)}")
#         time.sleep(0.01)  # Faster rendering

#         screenshot_path = f"{file_name_prefix}_zoom_{i}.png"
#         driver.save_screenshot(screenshot_path)
#         screenshots.append(screenshot_path)
    
#     driver.quit()
#     return screenshots

# # Function to create a smooth zoom-in video
# def create_zoom_video(screenshots, output_video_file):
#     clip = ImageSequenceClip(screenshots, fps=60)  # 60 FPS for smooth animation
#     clip = clip.resize(height=1080)  # Upgrade to 1080p
#     clip.write_videofile(output_video_file, codec="libx264", preset="slow")

# # Example usage:
# city_name = "Mumbai"
# screenshots = generate_map(city_name, zoom_level=5, file_name_prefix="zoom_mumbai")
# if screenshots:
#     create_zoom_video(screenshots, "zoom_mumbai_video.mp4")


import folium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from opencage.geocoder import OpenCageGeocode
from moviepy.editor import ImageSequenceClip
import numpy as np  # For smooth zoom interpolation

# Function to get city coordinates using OpenCage API
def get_city_coordinates(city_name):
    key = 'cb40be970fa24926b3b0cb4233b21f1e'  # Replace with your API key
    geocoder = OpenCageGeocode(key)
    result = geocoder.geocode(city_name)

    if result:
        lat = result[0]['geometry']['lat']
        lon = result[0]['geometry']['lng']
        return lat, lon
    else:
        print(f"Could not find coordinates for {city_name}.")
        return None

# Bézier curve interpolation for smooth zoom
def bezier_curve(t, p0, p1, p2):
    return (1 - t)**2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2

# Function to generate zoom-in effect with smooth motion
def generate_map(city_name, zoom_level, file_name_prefix):
    coords = get_city_coordinates(city_name)
    if not coords:
        return None
    
    screenshots = []
    frames = 300  # More frames for smoother motion

    # Bézier-based zoom transition for natural feel
    zoom_steps = [bezier_curve(t / frames, zoom_level, zoom_level * 2, zoom_level * 4) for t in range(frames)]

    lat_shift = 0.00005  # Even smaller shift for better smoothness
    lng_shift = 0.00005  

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1920x1080")  # Full HD
    options.add_argument("--start-maximized")
    options.add_argument("--enable-webgl")
    options.add_argument("--disable-software-rasterizer")

    driver = webdriver.Chrome(options=options)
    
    for i, zoom in enumerate(zoom_steps):
        lat = coords[0] + (i * lat_shift)
        lng = coords[1] + (i * lng_shift)

        initial_map = folium.Map(location=[lat, lng], zoom_start=zoom, tiles="OpenStreetMap")
        folium.Marker(location=[lat, lng], popup=city_name, icon=folium.Icon(color="red")).add_to(initial_map)

        map_html = "map.html"
        initial_map.save(map_html)

        driver.get(f"file://{os.path.abspath(map_html)}")
        time.sleep(0.005)  # Ultra-fast rendering

        screenshot_path = f"{file_name_prefix}_zoom_{i}.png"
        driver.save_screenshot(screenshot_path)
        screenshots.append(screenshot_path)
    
    driver.quit()
    return screenshots

# Function to create a smooth zoom-in video
def create_zoom_video(screenshots, output_video_file):
    clip = ImageSequenceClip(screenshots, fps=90)  # Increased FPS for smoother video
    clip = clip.resize(height=1080)  # 1080p quality
    clip.write_videofile(output_video_file, codec="libx264", preset="slow")

# Example usage:
city_name = "Mumbai"
screenshots = generate_map(city_name, zoom_level=5, file_name_prefix="zoom_mumbai")
if screenshots:
    create_zoom_video(screenshots, "zoom_mumbai_video.mp4")
