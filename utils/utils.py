#!/usr/bin/python3
"""
Utility Functions for Data Type Checking and Parsing

This module provides utility functions to check whether a given string can be
interpreted as an integer or a floating-point number, and a function to parse
a string into an int, float, or string based on its content. These functions are
useful for data validation and parsing in various contexts where numeric
data or potential string inputs are received as strings but need to be accurately
converted or evaluated to their respective types without causing errors.

Functions:
- is_integer(value): Checks if a string can be safely converted to an integer.
- is_floating_point(value): Determines if a string represents a floating-point number.
- parse_str(arg): Parses a string into an int, float, or string based on its content.
"""

import re

def is_integer(value):
    """
    Determines if the provided value can be converted to an integer.
    """
    try:
        float_value = float(value)
        int_value = int(float_value)
    except ValueError:
        return False
    else:
        return float_value == int_value

def is_float(value):
    """
    Checks if the value is a floating-point number.
    """
    try:
        _ = float(value)
    except ValueError:
        return False
    else:
        return True

def parse_str(arg):
    """
    Parses `arg` to an `int`, `float`, or `string` based on its content.
    """
    parsed = re.sub(r"\"", "", arg)

    if is_integer(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg
