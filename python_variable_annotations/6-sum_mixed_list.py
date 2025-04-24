#!/usr/bin/env python3
"""
This module provides a function to sum all the elements of a lists.
"""
from typing import List, Union
"""
Function to sum all the elements of a list
Args:
    input_list: list of floats and intergers
Returns:
    The sum of all the elements in the list
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function to sum all the elements of a list
    Args:
        input_list: list of floats and intergers
    Returns:
        The sum of all the elements in the list
    """
    return float(sum(mxd_lst))
