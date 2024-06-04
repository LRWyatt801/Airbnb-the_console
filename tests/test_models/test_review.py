#!/usr/bin/python3

import unittest
import uuid
from models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):
    """Tests for Review class"""

    def setUp(self):
        self.my_review = Review('this place stinks!')

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_review.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_review.created_at, datetime)
