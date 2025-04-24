#!/usr/bin/env python3
"""A simple example of a function with type hints."""
from typing import Iterable, Sequence, Tuple, List
"""
This function takes an iterable of
sequence-like elements (e.g., strings, lists)
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple
    contains an element from the iterable
    and the length of that element.

    Args:
        lst (Iterable[Sequence]): An iterable of
        sequence-like elements (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
