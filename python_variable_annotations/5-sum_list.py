#!/usr/bin/env python3
"""
This module provides a function to sum all the elements of a lists.
"""
from typing import List
"""
Function to sum all the elements of a list
"""


def sum_list(input_list: List[float]) -> float:
    """
    Function to sum all the elements of a list
    Args:
        input_list: list of floats
    Returns:
        The sum of all the elements in the list
    """
    return sum(input_list)
