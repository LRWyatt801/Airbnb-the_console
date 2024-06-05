#!/usr/bin/python3


import unittest
import uuid
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Tests for Place class"""

    def setUp(self):
        self.my_place = Place(
            '7b3568f4-c29e-4e2d-9349-d973d05a9fe8',
            '7363ab86-0c89-4b15-9922-8d3a1b53f1b5',
            'Roxford Ave',
            'Mansion',
            0,
            0,
            0,
            0,
            0.0,
            0.0,
            [
                '606ff695-20d9-4f24-859c-0ef52e6a1630'
            ])

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_place.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_place.created_at, datetime)

    def test_city_id(self):
        self.assertIsInstance(self.my_place.city_id, str)

    def test_user_id(self):
        self.assertIsInstance(self.my_place.user_id, str)

    def test_name(self):
        self.assertIsInstance(self.my_place.name, str)

    def test_num_features(self):
        self.assertIsInstance(self.my_place.number_rooms, int)
        self.assertIsInstance(self.my_place.number_bathrooms, int)
        self.assertIsInstance(self.my_place.max_guests, int)
        self.assertIsInstance(self.my_place.price_by_night, int)
        self.assertIsInstance(self.my_place.latitude, float)
        self.assertIsInstance(self.my_place.longitude, float)
        self.assertIsInstance(self.my_place.amenity_id, list)


if __name__ == '__main__':
    unittest.main()
