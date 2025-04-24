#!/usr/bin/env python3
"""
The function is designed to be simple and efficient.
"""
from typing import Callable
"""
This module provides a function to create a multiplier function.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function
        that takes a float and returns the product
                                  as a float.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
