#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""
    def __init__(self, place_id=None, user_id=None, text=""):
        super().__init__()

        self.place_id = place_id
        self.user_id = user_id
        self.text = text
