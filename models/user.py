#!/usr/bin/python3
"""define here the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """class user.

    Attributes:
        email (str): email of user.
        password (str): The user password.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
