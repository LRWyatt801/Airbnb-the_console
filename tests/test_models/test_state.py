#!/usr/bin/python3

import unittest
import uuid
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    """Tests for State class"""

    def setUp(self):
        self.my_state = State('Texas')

    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_state.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(self.my_state.created_at, datetime)

    def test_name(self):
        self.assertIsInstance(self.my_state.name, str)

if __name__ == '__main__':
    unittest.main()
