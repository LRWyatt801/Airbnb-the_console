#!/usr/bin/python3

import unittest
import uuid
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    """Tests for Place class"""

    def setUp(self):
        self.my_place = Place('Roxford Ave')

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_place.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_place.created_at, datetime)
