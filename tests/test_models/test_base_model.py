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
        original_update_time = self.my_base.updated_at
        self.my_base.save()
        self.assertNotEqual(self.my_base.updated_at, original_update_time)

    
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
    
    def test_from_dict(self):
        """test instance creation from dictionary"""
        my_model = BaseModel()  # create model
        my_model.name = "My_first_Model"
        my_model.number = 89
        my_model_json = my_model.to_dict()  # turn it into str
        my_new_model = BaseModel(**my_model_json)  # upload new instance
        
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertIsNot(my_model, my_new_model)
        

if __name__ == '__main__':
    unittest.main()
