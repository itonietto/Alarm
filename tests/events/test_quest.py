# -*- coding: utf-8 -*-

# Standard Library Imports
import unittest
# 3rd Party Imports
# Local Imports
from prototype.events import Quest


def generic_quest(values):
    """ Generate a generic quest, overriding with an specific values. """
    settings = {
        "pokestop_id": 0,
        "pokestop_name": "Stop Name",
        "pokestop_url": "http://placehold.it/500x500",
        "latitude": 37.7876146,
        "longitude": -122.390624,
        "quest": "Do Stuff",
        "reward": "Get Stuff",
        "type": 0
    }
    settings.update(values)
    return Quest(settings)


class TestStopEvent(unittest.TestCase):

    def test_lat(self):
        quest = generic_quest({'latitude': 0})
        self.assertTrue(isinstance(quest.lat, float))
        self.assertTrue(quest.lat == 0.0)

    def test_lng(self):
        quest = generic_quest({'longitude': 0})
        self.assertTrue(isinstance(quest.lng, float))
        self.assertTrue(quest.lng == 0.0)

    def test_stop_id(self):
        quest = generic_quest({'pokestop_id': 1})
        self.assertTrue(isinstance(quest.stop_id, str))
        self.assertTrue(quest.stop_id == "1")

    def test_stop_name(self):
        quest = generic_quest({'pokestop_name': 'Stop Name'})
        self.assertTrue(isinstance(quest.stop_name, str))
        self.assertTrue(quest.stop_name == "Stop Name")

    def test_stop_url(self):
        quest = generic_quest({'pokestop_url': 'http://placehold.it/1x1'})
        self.assertTrue(isinstance(quest.stop_image, str))
        self.assertTrue(quest.stop_image == "http://placehold.it/1x1")

    def test_quest(self):
        quest = generic_quest({'quest': 'Do Stuff'})
        self.assertTrue(isinstance(quest.quest, str))
        self.assertTrue(quest.quest == 'Do Stuff')

    def test_reward(self):
        quest = generic_quest({'reward': 'Get Stuff'})
        self.assertTrue(isinstance(quest.reward, str))
        self.assertTrue(quest.reward == 'Get Stuff')

    def test_expiry(self):
        quest = generic_quest({})
        self.assertTrue(isinstance(quest.expiry, str))

    def test_type(self):
        quest = generic_quest({'type': 7})
        self.assertTrue(isinstance(quest.type_id, int))
        self.assertTrue(quest.type_id == 7)
