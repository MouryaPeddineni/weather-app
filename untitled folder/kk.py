# import requests
# import folium
# import os
# from PIL import Image
# from io import BytesIO
# import os
# import time
# import folium
# from selenium import webdriver
# from PIL import Image

# # Ensure the "maps" folder exists
# MAPS_DIR = "maps"
# os.makedirs(MAPS_DIR, exist_ok=True)

# GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
# GOOGLE_CSE_ID = "3269dbbc6cdf0482b"
# GOOGLE_PLACES_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"


# def get_popular_places(city):
#     """Fetch popular tourist attractions in a city using Google Places API."""
    
#     query = f"tourist attractions in {city}"
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

#     return places

    
# import requests

# def search_image(query):
#     """Fetch an image using Google Custom Search API."""

#     url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         "q": query,
#         "cx": GOOGLE_CSE_ID,
#         "key": GOOGLE_API_KEY,
#         "searchType": "image",
#         "num": 1,
#     }

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }

#     try:
#         response = requests.get(url, params=params, headers=headers)
#         response.raise_for_status()
#         data = response.json()

#         # print(data)
#         # Extract image URLs
#         if "items" in data:
#             for item in data["items"]:
#                 image_url = item["link"]
#                 # Exclude blocked domains
#                 # if not any(domain in image_url for domain in ["wikimedia", "flickr"]):
#                 return image_url  # Return first non-blocked image

#         return "images/default.jpg"  # Fallback if all images are blocked
#     except requests.exceptions.RequestException as e:
#         print(f"⚠️ Error fetching image: {e}")
#         return "images/default.jpg"



# def create_map(lat, lon, city_name):
#     """Generate a map using folium, capture a screenshot using Selenium, and save it as a JPG."""
    
#     # Ensure the maps directory exists
#     os.makedirs("maps", exist_ok=True)
    
#     # Save Folium map as HTML
#     map_file = f"maps/{city_name}.html"
#     folium_map = folium.Map(location=[lat, lon], zoom_start=12)
#     folium.Marker(
#         [lat - 0.002, lon],  # Moves marker slightly downward
#         popup=city_name,
#         icon=folium.Icon(icon="cloud", color="blue"),  # Customizable icon
#     ).add_to(folium_map)

#     folium_map.save(map_file)

#     # Set up Selenium WebDriver (headless mode)
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--window-size=800x600")  # Set window size for proper screenshot
    
#     driver = webdriver.Chrome(options=options)
#     driver.get(f"file://{os.path.abspath(map_file)}")
#     time.sleep(2)  # Wait for the page to load
    
#     # Save the screenshot as PNG
#     screenshot_path = f"maps/{city_name}.png"
#     driver.save_screenshot(screenshot_path)
#     driver.quit()
    
#     # Convert PNG to JPG
#     img = Image.open(screenshot_path)
#     jpg_path = f"maps/{city_name}_img.jpg"
#     img.convert("RGB").save(jpg_path, "JPEG")

#     # Remove the original PNG file
#     os.remove(screenshot_path)

#     print(f"✅ Map saved as {jpg_path}")
#     return jpg_path


# def save_map_as_image(city):
#     """Generate a Folium map and save it as an image with an overlay above the marker."""
#     places = get_popular_places(city)
#     # print(places)

#     if not places:
#         print(f"⚠️ No popular places found in {city}.")
#         return None

#     img_url = None
#     popular_place = None

#     # Iterate over popular places to find one with a valid image
#     for place in places:
#         print(f"Checking: {place['name']}")
#         img_url = search_image(place["name"])
#         if img_url and "Hyderabad.jpg" not in img_url:  # Ensure it's not the placeholder
#             popular_place = place
#             break  # Stop searching once a valid image is found

#     if not popular_place:
#         print("⚠️ No valid image found for any popular places.")
#         return None
    
#     # lat, lon = popular_place["lat"], popular_place["lon"]
#     # print(f"Selected place: {popular_place['name']}")
#     print(f"Image URL: {img_url}")

#     # Create a map centered around the selected place
#     city_map_path = create_map(12.9716, 77.5946, city)

#     if not os.path.exists(city_map_path):
#         print(f"⚠️ Map image not found: {city_map_path}")
#         return None

#     # Open the city map image
#     map_image = Image.open(city_map_path)

#     # Fetch the place image
#     place_image = None
#     if img_url:
#         try:
#             headers = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#             }

#             img_response = requests.get(img_url, headers=headers)
#             print(img_response)
#             img_response.raise_for_status()  # Ensure the request was successful
#             # print(img_response.content)
#             place_image = Image.open(BytesIO(img_response.content))
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Failed to fetch image for {popular_place['name']}: {e}")

#     # If no valid place image is found, use a placeholder
#     if place_image is None:
#         place_image = Image.new("RGB", (100, 100), color=(200, 200, 200))  # Grey placeholder

#     # Resize the place image to 20% of the map size
#     overlay_size = (int(map_image.width * 0.2), int(map_image.height * 0.4))
#     place_image = place_image.resize(overlay_size)

#     # Approximate marker position
#     marker_x = map_image.width // 2
#     marker_y = map_image.height // 2

#     # Place the overlay just above the marker (adjust Y-coordinate)
#     position = (marker_x - overlay_size[0] // 2 - 400, marker_y - overlay_size[1])
# # Centered horizontally, 10px above

#     if place_image.mode == 'RGBA':
#         map_image.paste(place_image, position, place_image)
#     else:
#         map_image.paste(place_image, position)

#     # Save the final image as a JPG
#     final_image_path = os.path.join(MAPS_DIR, f"{city}_map_final.jpg")
#     map_image.convert("RGB").save(final_image_path, "JPEG")

#     print(f"✅ Final map with overlay saved: {final_image_path}")
#     return final_image_path


# # Example usage
# save_map_as_image("Bangalore")


import requests
import folium
import os
import time
from selenium import webdriver
from PIL import Image, ImageDraw, ImageOps
from io import BytesIO

# Ensure the "maps" folder exists
MAPS_DIR = "maps"
os.makedirs(MAPS_DIR, exist_ok=True)

GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
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


def create_map(lat, lon, city_name):
    """Generate a map and capture a screenshot as an image."""
    map_file = f"maps/{city_name}.html"
    folium_map = folium.Map(location=[lat, lon], zoom_start=12)
    # folium.Marker(
    #     [lat - 0.002, lon], popup=city_name, icon=folium.Icon(icon="cloud", color="blue")
    # ).add_to(folium_map)

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


def create_marker_shape(image):
    """Convert the fetched image into a marker shape with a larger rounded top and tapered bottom."""
    size = image.size
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)

    # Increase the height of the rounded top
    rounded_top_height = int(size[1] * 0.80)  # Increased from 0.70 to 0.80

    draw.ellipse((0, 0, size[0], rounded_top_height), fill=255)  # Larger rounded top
    draw.polygon(
        [(size[0] // 2, size[1] * 0.95), (0, size[1] * 0.5), (size[0], size[1] * 0.5)], fill=255
    )  # Pointed bottom

    # Apply the mask
    marker_image = ImageOps.fit(image, size, centering=(0.5, 0.5))
    marker_image.putalpha(mask)

    return marker_image



def save_map_as_image(city):
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

    # Create a city map image
    city_map_path = create_map(17.4065, 78.4772, city)

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
    place_image = create_marker_shape(place_image)

    # Approximate marker position
    marker_x = map_image.width // 2
    marker_y = map_image.height // 2

    # Place the overlay just above the marker
    position = (marker_x - overlay_size[0] // 2, marker_y - overlay_size[1] - 10)

    map_image.paste(place_image, position, place_image)

    # Save the final image
    final_image_path = os.path.join(MAPS_DIR, f"{city}_map_final.jpg")
    map_image.convert("RGB").save(final_image_path, "JPEG")

    print(f"✅ Final map with marker-shaped overlay saved: {final_image_path}")
    return final_image_path


# Example usage
save_map_as_image("Hyderabad")
