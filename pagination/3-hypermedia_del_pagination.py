#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
# import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        returns a dictionary with a page of data using the index and size of
        the page, filling in the missing data with the next data
        so that the page remains complete
        """
        assert isinstance(index, int) and isinstance(page_size, int)
        assert 0 <= index < len(self.indexed_dataset())
        page_data = []
        next_index = index
        while len(page_data) < page_size and\
                next_index < len(self.indexed_dataset()):
            if self.indexed_dataset().get(next_index):
                page_data.append(self.indexed_dataset()[next_index])
            next_index += 1
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": page_data
        }
