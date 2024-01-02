#!/usr/bin/env python3
"""this module contains a dunction definition"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this function returns a touple of string and squared float"""
    return (k, v**2)
