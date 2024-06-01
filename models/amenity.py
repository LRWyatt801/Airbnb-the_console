#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity"""
    def __init__(self, name=""):
        super().__init__()

        self.name = name
