#!/usr/bin/python3
"""The `state` module

Defines class `State()`,
which sub-classes the `BaseModel()` class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.

    Attributes:
        name
    """
    name = ""