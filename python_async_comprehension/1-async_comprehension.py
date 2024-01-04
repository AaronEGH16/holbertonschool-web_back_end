#!/usr/bin/env python3
"""
this module contains an async function
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    this function makes a list of async items
    using list comprehension
    """
    return [item async for item in async_generator()]
