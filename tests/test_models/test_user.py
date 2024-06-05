#!/usr/bin/python3

import unittest
import uuid
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    """Tests for Userclass"""

    def setUp(self):
        self.my_user = User('email', 1234, 'Dougie', 'Jones')

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_user.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_user.created_at, datetime)

    def test_attrs(self):
        self.assertFalse(isinstance(self.my_user.password, int))
        self.assertTrue(isinstance(self.my_user.email, str))
        self.assertTrue(isinstance(self.my_user.first_name, str))
        self.assertTrue(isinstance(self.my_user.last_name, str))

if __name__ == '__main__':
    unittest.main()
