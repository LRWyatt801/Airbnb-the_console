#!/usr/bin/python3


import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        self.my_base = BaseModel()
    
    def test_id(self):
        self.assertTrue(uuid.UUID(self.my_base.id, version=4))
    
    def test_created_at(self):
        self.assertIsInstance(self.my_base.created_at, datetime)
    
    def test_save(self):
        self.my_base.save()
        self.assertEqual(self.my_base.updated_at, self.my_base.created_at)
        self.assertIsInstance(self.my_base.updated_at, datetime)
    
    def test_to_dict(self):
        self.assertIsInstance(self.my_base.to_dict(), dict)
    
    def test_str(self):
        # self.my_base.id = 42
        # self.assertMultiLineEqual(print(self.my_base), )
        pass