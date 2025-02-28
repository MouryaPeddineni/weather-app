# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import time

# # Function to open the animated map and record it
# def open_map_animation():
#     options = Options()
#     options.add_argument("--start-maximized")
    
#     # Open Chrome browser
#     driver = webdriver.Chrome(options=options)
#     file_path = "file://" + os.path.abspath("map_view.html")
#     driver.get(file_path)

#     # Allow the animation to start
#     time.sleep(5)

#     # Start recording with FFmpeg (Linux users: install FFmpeg first)
#     ffmpeg_command = "ffmpeg -y -f avfoundation -framerate 30 -i 1 -t 5 -r 60 -vcodec libx264 smooth_zoom.mp4"
#     os.system(ffmpeg_command)

#     # Close the browser
#     driver.quit()

# # Run the animation and record it
# open_map_animation()


# import asyncio
# from pyppeteer import launch
# import os
# import time
# import subprocess

# # Function to generate video from HTML file
# async def capture_screenshots():
#     # Launch headless browser
#     browser = await launch(headless=True)
#     page = await browser.newPage()

#     # Load the HTML file
#     file_path = 'file://' + os.path.abspath("map_view.html")
#     await page.goto(file_path)

#     # Capture screenshots every 0.1 second for 5 seconds (adjust as needed)
#     for i in range(50):  # 50 frames for 5 seconds at 10 FPS
#         screenshot_path = f"screenshots/frame_{i:03d}.png"
#         await page.screenshot({'path': screenshot_path})
#         time.sleep(0.1)

#     # Close the browser
#     await browser.close()

# # Function to create a video from the captured frames
# def create_video():
#     # Run FFmpeg to generate video from the screenshots
#     ffmpeg_command = [
#         'ffmpeg', '-y', '-framerate', '10', '-i', 'screenshots/frame_%03d.png', 
#         '-vcodec', 'libx264', '-pix_fmt', 'yuv420p', 'smooth_zoom.mp4'
#     ]
#     subprocess.run(ffmpeg_command)

# # Main function
# def generate_video():
#     # Create a directory for screenshots if it doesn't exist
#     os.makedirs('screenshots', exist_ok=True)

#     # Capture screenshots
#     asyncio.get_event_loop().run_until_complete(capture_screenshots())

#     # Create video from the screenshots
#     create_video()

#     # Cleanup: Remove screenshot images after video is created
#     for filename in os.listdir('screenshots'):
#         file_path = os.path.join('screenshots', filename)
#         os.remove(file_path)
#     os.rmdir('screenshots')

# # Run the process
# generate_video()


# import asyncio
# from pyppeteer import launch
# import os
# import time
# from moviepy.editor import ImageSequenceClip

# # Function to render HTML and capture frames
# async def capture_frames():
#     browser = await launch(headless=True)
#     page = await browser.newPage()

#     # Load the HTML file
#     file_path = 'file://' + os.path.abspath("map_view.html")
#     await page.goto(file_path)

#     # Capture frames at intervals (e.g., every 0.1 second)
#     frames = []
#     for i in range(50):  # Capture 50 frames for a 5-second video
#         screenshot_path = f"screenshots/frame_{i:03d}.png"
#         await page.screenshot({'path': screenshot_path})
#         frames.append(screenshot_path)
#         time.sleep(0.1)  # Capture frames at 10 FPS

#     await browser.close()
#     return frames

# # Function to create video from captured frames using MoviePy
# def create_video(frames):
#     # Create a video from the screenshots (adjust fps as needed)
#     clip = ImageSequenceClip(frames, fps=10)  # 10 FPS
#     clip.write_videofile("smooth_zoom.mp4", codec="libx264")

# # Main function to generate the video
# def generate_video():
#     # Create a directory for screenshots if it doesn't exist
#     os.makedirs('screenshots', exist_ok=True)

#     # Capture frames
#     frames = asyncio.get_event_loop().run_until_complete(capture_frames())

#     # Create video from frames
#     create_video(frames)

#     # Clean up: Delete the screenshots after the video is generated
#     for frame in frames:
#         os.remove(frame)
#     os.rmdir('screenshots')

# # Run the process
# generate_video()
