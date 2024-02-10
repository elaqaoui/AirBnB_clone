#!/usr/bin/env python3

# This module defines a class named 'Review' that inherits from 'BaseModel'.
from models.base_model import BaseModel

class Review(BaseModel):
# Public class attributes:
# - place_id: A string initialized with an empty string, representing the Place.id.
# - user_id: A string initialized with an empty string, representing the User.id.
# - text: A string initialized with an empty string.

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # check if kwargs have values anymore.
        if len(kwargs) > 0:
            super().__init__(**kwargs)
