#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """class State"""
    def __init__(self, name=""):
        super().__init__()

        self.name = name
