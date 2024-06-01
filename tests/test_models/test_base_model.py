#!/usr/bin/python3


import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        """create new instance for each test"""
        self.my_base = BaseModel()
    
    def test_id(self):
        """test the id attribute"""
        self.assertTrue(uuid.UUID(self.my_base.id, version=4))
    
    def test_created_at(self):
        """test the created_at attribute"""
        self.assertIsInstance(self.my_base.created_at, datetime)
    
    def test_save(self):
        """test the save method"""
        self.my_base.save()
        self.assertIsInstance(self.my_base.updated_at, datetime)
        self.assertNotEqual(self.my_base.updated_at, self.my_base.created_at)

    
    def test_to_dict(self):
        """test the to_dict method"""
        self.assertIsInstance(self.my_base.to_dict(), dict)
        expected_dict = {
            'id': self.my_base.id,
            'created_at': self.my_base.created_at.isoformat(),
            '__class__': self.my_base.__class__.__name__,
            'updated_at': self.my_base.updated_at.isoformat(),
        }
        self.assertEqual(self.my_base.to_dict(), expected_dict)
    
    def test_str(self):
        """test the __str__ method"""
        expected_output = "[{}] ({}) {}".format(
            self.my_base.__class__.__name__,
            self.my_base.id,
            self.my_base.__dict__
        )
        self.assertEqual(str(self.my_base), expected_output)

if __name__ == '__main__':
    unittest.main()