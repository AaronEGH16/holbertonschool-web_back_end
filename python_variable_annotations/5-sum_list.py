#!/usr/bin/env python3
"""
this module contains a function definition
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    this function returns a sum of all list elements
    """
    res = 0.0
    for num in input_list:
        res += num
    return res
