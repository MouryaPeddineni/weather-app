import folium
import time
from selenium import webdriver
from PIL import Image, ImageEnhance
import moviepy as mpy
import os

MAPS_DIR = "maps"
os.makedirs(MAPS_DIR, exist_ok=True)

# Step 1: Generate Folium Map
map_center = [12.9716, 77.5946]  # Example: Bangalore coordinates
m = folium.Map(location=map_center, zoom_start=12)

# Add a Marker
folium.Marker(map_center, popup="Bangalore", tooltip="Click for more").add_to(m)

map_file = f"maps/Bengaluru.html"
# folium_map = folium.Map(location=[lat, lon], zoom_start=12)

m.save(map_file)

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=800x600")

driver = webdriver.Chrome(options=options)
driver.get(f"file://{os.path.abspath(map_file)}")
time.sleep(2)

screenshot_path = f"maps/Bengaluru.png"
driver.save_screenshot(screenshot_path)
driver.quit()

# Convert PNG to JPG
img = Image.open(screenshot_path)
jpg_path = f"maps/Bengaluru_img.jpg"
img.convert("RGB").save(jpg_path, "JPEG")
# os.remove(screenshot_path)

print(f"✅ Map saved as {jpg_path}")



# Save the map as an HTML file
# map_path = "map.html"
# m.save(map_path)

# # Step 2: Convert HTML to Image using Selenium
# driver = webdriver.Chrome()  # Ensure you have a driver installed
# driver.get(f"file:///{map_path}")
# time.sleep(2)  # Allow time for map to load

# # Capture Screenshot
# screenshot_path = "map_screenshot.png"
# driver.save_screenshot(screenshot_path)
# driver.quit()

# Step 3: Open Image and Add an Alpha Channel
image = Image.open(screenshot_path).convert("RGBA")
width, height = image.size

# Create an Alpha Layer (Gradient or Overlay)
alpha_layer = Image.new("L", (width, height), 100)  # Adjust transparency
image.putalpha(alpha_layer)

# Step 4: Save and Convert Images to Video
image.save("enhanced_map.png")

# Convert to Video using MoviePy
clip = mpy.ImageSequenceClip(["enhanced_map.png"] * 30, fps=10)  # 3-sec video
clip.write_videofile("map_video.mp4", codec="libx264")
