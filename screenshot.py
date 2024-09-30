import pyautogui
from io import BytesIO
from PIL import Image

class ScreenshotManager:
    def __init__(self, config):
        self.config = config

    def capture_screenshot(self):
        # Capture a screenshot using pyautogui
        screenshot = pyautogui.screenshot()

        # Save the screenshot to a BytesIO object
        img_byte_arr = BytesIO()
        screenshot.save(img_byte_arr, format='JPEG')

        # Return the byte data of the image
        return img_byte_arr

    def capture_and_save_screenshot(self, filepath):
        screenshot = pyautogui.screenshot()
        screenshot.save(filepath)
        print(f"Screenshot saved to {filepath}")
