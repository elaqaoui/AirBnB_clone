#!/usr/bin/env python3
# This module defines a class named 'User' that inherits from 'BaseModel'.

from models.base_model import BaseModel


class User(BaseModel):
# Public class attributes:
# - email: A string initialized with an empty string.
# - password: A string initialized with an empty string.
# - first_name: A string initialized with an empty string.
# - last_name: A string initialized with an empty string.

    last_name = ''
    first_name = ''
    email = ''
    password = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
