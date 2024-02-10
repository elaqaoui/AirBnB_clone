#!/usr/bin/env python3
# Place Module
# This module includes and manages the Place Entity.

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

    user_id = ''
    name = ''
    city_id = ''
    number_rooms = 0
    amenity_ids = []
    description = ''
    number_bathrooms = 0
    price_by_night = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0

    # Check if keyword arguments are provided
    def __init__(self, *args, **kwargs):

        '''
    Initializes the object with optional positional or keyword arguments.
    If no keyword arguments are provided, it initializes the object using default values.
    If keyword arguments are provided, it passes them to the superclass's __init__ method.
        '''

        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
