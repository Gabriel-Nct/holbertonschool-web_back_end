#!/usr/bin/env python3
"""
Function named index_range that takes
two integer arguments page and page_size
"""
import csv
from typing import List
"""
importing module csv and list
"""


def index_range(page: int, page_size: int):
    """
    function should return a tuple of size two containing
    a start index and an end index corresponding to the range of indexes
    Args:
        page (int): number of the page to display
        page_size (int): number of element to displays
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on pagination parameters
        Args:
            page (int): Page number (1-indexed)
            page_size (int): Number of records per page
        Returns:
            List[List]: List of rows in the specified page range
        """
        assert isinstance(page, int) and page > 0, "must be a +int"
        assert isinstance(page_size, int) and page_size > 0, "must be a +int"

        dataset = self.dataset()

        start_idx, end_idx = index_range(page, page_size)

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]
