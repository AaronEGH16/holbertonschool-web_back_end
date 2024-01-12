#!/usr/bin/env python3
"""
this module contains a definition of "index_range" function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    this function get page and size and returns a Tuple
    of size 2: tuple(start index, end index)
    """
    return (((page - 1) * page_size), (((page - 1) * page_size) + page_size))
