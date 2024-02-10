#!/usr/bin/env python3

# State Module
# This module includes and manages the State Entity.

from models.base_model import BaseModel


class State(BaseModel):
# Public class attributes:
# - name: A string initialized with an empty string.

    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # check if kwargs have values anymore
        if len(kwargs) > 0:
            super().__init__(**kwargs)
