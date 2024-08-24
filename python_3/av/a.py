import pyautogui

# Open the camera
cam = pyautogui.openCamera()

# Take a screenshot from the camera
img = cam.read()

# Save the screenshot to a file
img.save('camera_screenshot.png')