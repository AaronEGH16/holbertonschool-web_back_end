#!/usr/bin/env python3
"""
this module contains an async function
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to "wait_n" except
    "task_wait_random" is being called.
    """
    wait_list = [task_wait_random(max_delay) for _ in range(n)]
    list_delay = await asyncio.gather(*wait_list)
    return sorted(list_delay)
