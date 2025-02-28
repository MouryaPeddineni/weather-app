# import requests

# API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
# city = "Bangalore"
# query = f"tourist attractions in {city}"
# url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={API_KEY}"

# response = requests.get(url)
# data = response.json()

# if "error_message" in data:
#     print(f"⚠️ API Error: {data['error_message']}")
# else:
#     print(data)

# import folium
# import requests
# from PIL import Image
# from io import BytesIO

# GOOGLE_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"
# GOOGLE_CSE_ID = "3269dbbc6cdf0482b"
# GOOGLE_PLACES_API_KEY = "AIzaSyCFok1h4tkAF3KO_53oSrxIYLMUo_poHO8"

# # Your image search function
# def search_image(query):
#     """Fetch an image using Google Custom Search API."""
    
#     url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         "q": query,
#         "cx": GOOGLE_CSE_ID,
#         "key": GOOGLE_API_KEY,
#         "searchType": "image",
#         "num": 5,  # More images to filter
#     }
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }

#     try:
#         response = requests.get(url, params=params, headers=headers)
#         response.raise_for_status()
#         data = response.json()

#         # print(data)

#         # Filter out Wikimedia & Flickr
#         if "items" in data:
#             for item in data["items"]:
#                 image_url = item["link"]
#                 # if not any(domain in image_url for domain in ["wikimedia", "flickr"]):
#                 return image_url  # First valid image
#         return None  # No valid image
#     except requests.exceptions.RequestException as e:
#         print(f"⚠️ Error fetching image: {e}")
#         return None

# # Fetch image for Tipu Sultan's Palace
# query = "Tipu Sultan's Summer Palace"
# image_url = search_image(query)
# print(image_url)

# if image_url:
#     # Download image and resize it for marker
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     img_response = requests.get(image_url, headers = headers)
#     # print(img_response)
#     img = Image.open(BytesIO(img_response.content))
#     img = img.resize((50, 50))  # Resize for marker

#     # Save locally
#     img_path = "marker_image.png"
#     img.save(img_path)

#     # Create map
#     m = folium.Map(location=[12.9592, 77.5736], zoom_start=15)  # Tipu Sultan's Palace coords

#     # Add custom image as marker
#     icon = folium.CustomIcon(img_path, icon_size=(50, 50))  # Custom marker with image
#     folium.Marker([12.9592, 77.5736], icon=icon, popup=query).add_to(m)

#     # Save map as HTML
#     m.save("map.html")
#     print("✅ Map saved as map.html with custom marker!")


import requests

url = "https://api.weatherapi.com/v1/current.json?key=22cd9db3340944d697b173414252401&q=17.686915,83.218481"
response = requests.get(url)

print(response.json())  # Check response
