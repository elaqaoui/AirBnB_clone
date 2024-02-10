#!/usr/bin/env python3
# This module defines a class named 'City' that inherits from 'BaseModel'.

from models.base_model import BaseModel

class City(BaseModel):
  # Public class attributes:
  # - state_id: A string initialized with an empty string, representing the State.id.
  # - name: A string initialized with an empty string.

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        ''' if kwargs have values '''

        if len(kwargs) > 0:
            super().__init__(**kwargs)
