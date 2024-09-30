import time
from activity_tracker import ActivityTracker
from screenshot import ScreenshotManager
from config import ConfigManager
from uploader import S3Uploader

class Agent:
    def __init__(self):
        self.config = ConfigManager()
        self.activity_tracker = ActivityTracker()
        self.screenshot_manager = ScreenshotManager(self.config)
        self.uploader = S3Uploader(self.config)

    def run(self):
        while True:
            if self.config.is_screenshot_enabled():
                screenshot = self.screenshot_manager.capture_screenshot()
                compressed_screenshot = self.screenshot_manager.compress_screenshot(screenshot)
                self.uploader.upload(compressed_screenshot)

            user_activity = self.activity_tracker.track_activity()
            if user_activity.is_suspicious():
                print("Suspicious activity detected.")
            time.sleep(self.config.get_screenshot_interval())

if __name__ == "__main__":
    agent = Agent()
    agent.run()
