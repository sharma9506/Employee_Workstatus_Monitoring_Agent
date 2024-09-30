import unittest
from agent import Agent

class TestAgent(unittest.TestCase):
    def test_activity_detection(self):
        agent = Agent()
        activity = agent.activity_tracker.track_activity()
        self.assertFalse(activity.is_suspicious())

    # Additional tests

if __name__ == '__main__':
    unittest.main()
