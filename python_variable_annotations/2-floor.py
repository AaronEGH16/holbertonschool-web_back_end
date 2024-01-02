#!/usr/bin/env python3
"""
this module contains a definition of floor function
"""


def floor(n: float) -> int:
    """
    this function returns the lower integer more near
    to "n"
    """
    if n >= 0:
        return int(n)
    else:
        return int(n - 1)
