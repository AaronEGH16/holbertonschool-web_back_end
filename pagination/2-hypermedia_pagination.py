#!/usr/bin/env python3
"""
this module contains a definition of index_range function
and the definition of Server class
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    this function get page and size and returns a Tuple
    of size 2: tuple(start index, end index)
    """
    return (((page - 1) * page_size), (((page - 1) * page_size) + page_size))


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
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get the page indexed using page number and page_size and returns
        a list of all page elements
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        page_index = index_range(page, page_size)
        return self.dataset()[page_index[0]:page_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get the indexed page using page number and page size and
        returns a dict of all the information on the page:
            page_size: page size
            page: page number
            data: list of all elements on the page
            next_page: number of the next page or None if it is the last page
            prev_page: number of the prev page or None if it is the first page
            total_pages: number of total pages in the document
        """
        page_index = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        page_dict = {
            "page_size": len(page_index),
            "page": page,
            "data": page_index,
            "next_page": None if page >= total_pages else page + 1,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": total_pages
        }
        return page_dict
