#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """class City"""
    def __init__(self, state_id="", name=""):
        super().__init__()

        self.state_id = str(state_id)
        self.name = name
