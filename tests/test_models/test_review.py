#!/usr/bin/python3


import unittest
import uuid
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Tests for Review class"""

    def setUp(self):
        self.my_review = Review('userid', 'place_id', 'text')

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_review.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_review.created_at, datetime)

    def test_user_id(self):
        self.assertIsInstance(self.my_review.user_id, str)

    def test_place_id(self):
        self.assertIsInstance(self.my_review.place_id, str)

    def test_text(self):
        self.assertIsInstance(self.my_review.text, str)


if __name__ == '__main__':
    unittest.main()
