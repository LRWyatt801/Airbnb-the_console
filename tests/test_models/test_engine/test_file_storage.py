#!/usr/bin/python3
"""unittest for file_storage"""


import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    """tests for FileStorage class"""

    @classmethod
    def setUpClass(self) -> None:
        self.my_model = BaseModel()
        self.my_model.save()
        self.storage = storage

    def test__file_path(self):
        """test if __file_path exists"""
        self.assertTrue(os.path.exists('file.json'))

    def test_objects(self):
        self.assertIsInstance(storage.all(), dict)

    def test_all(self):
        expected_return = storage.all()
        self.assertIs(storage.all(), expected_return)

    def test_save(self):
        self.new_model = BaseModel()
        self.new_model.save()
        self.new_data = self.storage.reload()
        self.assertEqual(self.new_data, self.storage.reload())

    def test_new_and_save(self):
        self.instance = BaseModel()
        self.storage.new(self.instance)
        self.storage.save()
        with open('file.json', 'r') as file:
            data = json.load(file)
        self.assertIn("BaseModel.{}".format(self.instance.id), data)

    def test_reload(self):
        self.instance = BaseModel()
        self.storage.new(self.instance)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.instance.id}", self.storage.all())


if __name__ == "__main__":
    unittest.main()
