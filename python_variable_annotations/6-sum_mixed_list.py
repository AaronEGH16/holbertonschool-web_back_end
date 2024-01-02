#!/usr/bin/env python3
"""this module contains a function definition"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """this function sum all list elements"""
    res = 0.0
    for num in mxd_lst:
        res += num
    return res
