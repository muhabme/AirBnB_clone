#!/usr/bin/python3
"""The `review` module.

Defines class `State()`,
which sub-classes the `BaseModel()` class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review of a place.

    It represents a review posted by a user
    of the application about a place.

    Attributes:
        text
        user_id
        place_id
    """
    text = ""
    user_id = ""
    place_id = ""