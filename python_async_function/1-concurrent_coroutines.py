#!/usr/bin/env python3
"""
this module contains an async function
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function calls "wait_random" function "n"
    times passing max_delay var,
    and returns a sorted list with the awaited "n" times
    """
    wait_list = [wait_random(max_delay) for _ in range(n)]
    list_delay = await asyncio.gather(*wait_list)
    return sorted(list_delay)
