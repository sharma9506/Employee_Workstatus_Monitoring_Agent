import json
import time

class ConfigManager:
    def __init__(self):
        self.config_file = "config.json"
        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            self.config_data = json.load(file)

    def get_screenshot_interval(self):
        return self.config_data.get('screenshot_interval', 300)  # Default: 5 minutes

    def is_screenshot_enabled(self):
        return self.config_data.get('screenshot_enabled', True)

    def should_blur_screenshots(self):
        return self.config_data.get('blur_screenshots', False)

    def check_for_updates(self):
        while True:
            # Polling or listening for changes from a web app (e.g., using requests to fetch config)
            time.sleep(60)  # Check for config updates every minute
            self.load_config()

