#!/usr/bin/env python3
"""
This module provides a function to return the floor of a float as an integer.
"""
import math
"""
This function takes a float and returns
the largest integer less than or equal to it.
"""


def floor(n: float) -> int:
    """Return the largest integer less than or equal to n."""
    return int(math.floor(n))
