#!/usr/bin/env python3
"""
Function named index_range that takes two integer arguments page and page_size
"""


def index_range(page: int, page_size: int):
    """
    function should return a tuple of size two containing
    a start index and an end index corresponding to the range of indexes
    Args:
        page (int): number of the page to display
        page_size (int): ,umber of element to displays
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
