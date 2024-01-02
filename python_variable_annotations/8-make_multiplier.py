#!/usr/bin/env python3
"""
this module contains a function definition
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this function calls anidated function to get value and return it
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
