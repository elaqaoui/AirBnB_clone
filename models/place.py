#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
# Public class attributes:
# - city_id (str): A string initialized with an empty string, representing the City.id.
# - user_id (str): A string initialized with an empty string, representing the User.id.
# - name (str): A string initialized with an empty string.
# - description (str): A string initialized with an empty string.
# - number_rooms (int): Initialized with 0.
# - number_bathrooms (int): Initialized with 0.
# - max_guest (int): Initialized with 0.
# - price_by_night (int): Initialized with 0.
# - latitude (float): Initialized with 0.0.
# - longitude (float): Initialized with 0.0.
# - amenity_ids (list): An empty list of strings, which will represent the list of Amenity.id.

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
