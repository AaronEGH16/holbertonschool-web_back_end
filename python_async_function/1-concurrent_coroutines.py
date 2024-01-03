#!/usr/bin/env python3
"""
this module contains an async function
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    this function calls "wait_random" function "n"
    times passing max_delay var,
    and returns a sorted list with the awaited "n" times
    """
    wait_list = [await wait_random(max_delay) for _ in range(n)]
    wait_list.sort()
    return wait_list
