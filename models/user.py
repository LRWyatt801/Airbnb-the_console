#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """class User"""
    def __init__(self, email="", password="", first_name="", last_name=""):
        super().__init__()

        self.email = str(email)
        self.password = str(password)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
