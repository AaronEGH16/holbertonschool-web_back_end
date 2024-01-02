#!/usr/bin/env python3
"""
this module contains a function definition
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    this function returns a list of touples containing
    each sequence item and its length
    """
    return [(i, len(i)) for i in lst]
