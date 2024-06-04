#!/usr/bin/python3
"""contains a class FileStorage"""


import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = 'file.json'  # path to the JSON file

    # objects will store all objects by <classname>.id
    # ex: to store BaseModel object with id=1212,
    # the key will be BaseModel.1212
    __objects = {}

    def all(self) -> dict:
        """returns __objects

        Returns:
            dict: dictionary of objects
        """
        return self.__objects

    def new(self, obj) -> None:
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self) -> None:
        obj_to_dict = {}
        for key, value in self.__objects.items():
            # convert objects to dictionary
            obj_to_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            # write in file as JSON
            file.write(json.dumps(obj_to_dict))

    def reload(self) -> None:
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_instance = eval(class_name)(**value)
                self.__objects[key] = obj_instance

    @property
    def file_path(self):
        return self.__file_path
