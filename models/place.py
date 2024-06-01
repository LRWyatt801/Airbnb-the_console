#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """class Place"""
    def __init__(self, city_id=None, user_id=None, name="", 
                 description="", number_rooms=0, 
                 number_bathrooms=0, max_guests=0,
                 price_by_night=0, latitude=0,
                 longitude=0,
                 amenity_id=None):
        super().__init__()

        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guests = max_guests
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_id = amenity_id
