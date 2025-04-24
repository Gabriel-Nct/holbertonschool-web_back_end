#!/usr/bin/env python3
"""
The function takes two float arguments and returns their sum as a float.
"""
from typing import Tuple, Union
"""
This module provides a function to convert a key
and value to a tuple of the key and the square of the value.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to convert a key and value
    to a tuple of the key and the square of the value
    Args:
        k: key
        v: value
    Returns:
        A tuple of the key and the square of the value
    """
    return (k, float(v * v))
