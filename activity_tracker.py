import random

class ActivityTracker:
    def __init__(self):
        self.suspicious_patterns = ["irregular_mouse", "unnatural_keyboard"]

    def track_activity(self):
        # Logic to track real user activity, e.g., mouse movements, keystrokes
        activity_data = self.get_activity_data()

        # Check if activity looks suspicious
        if self.detect_suspicious_activity(activity_data):
            return SuspiciousActivity()

        return GenuineActivity()

    def get_activity_data(self):
        # Simulate activity capture (this should be replaced with real code)
        activity_data = {
            "mouse_movement": random.choice(["regular", "irregular"]),
            "keyboard_input": random.choice(["natural", "unnatural"])
        }
        return activity_data

    def detect_suspicious_activity(self, activity_data):
        if activity_data["mouse_movement"] == "irregular" or activity_data["keyboard_input"] == "unnatural":
            return True
        return False

class SuspiciousActivity:
    def is_suspicious(self):
        return True

class GenuineActivity:
    def is_suspicious(self):
        return False
