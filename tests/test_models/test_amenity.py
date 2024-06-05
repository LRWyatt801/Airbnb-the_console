#!/usr/bin/python3


import unittest
import uuid
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Tests for Amenity class"""

    def setUp(self):
        self.my_amenity = Amenity('Running Water')

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_amenity.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_amenity.created_at, datetime)

    def test_name(self):
        self.assertIsInstance(self.my_amenity.name, str)


if __name__ == "__main__":
    unittest.main()
