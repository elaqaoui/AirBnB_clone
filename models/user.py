#!/usr/bin/python3
"""class Definition of the User class."""
from models.base_model import BaseModel


class User(BaseModel):
# Public class attributes:
# - email: A string initialized with an empty string.
# - password: A string initialized with an empty string.
# - first_name: A string initialized with an empty string.
# - last_name: A string initialized with an empty string.

    email = ""
    password = ""
    first_name = ""
    last_name = ""
