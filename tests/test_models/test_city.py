#!/usr/bin/python3


import unittest
import uuid
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Tests for City class"""

    def setUp(self):
        self.my_city = City('Tulsa')

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_city.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_city.created_at, datetime)

    def test_name(self):
        self.assertIsInstance(self.my_city.name, str)

if __name__ == '__main__':
    unittest.main()
