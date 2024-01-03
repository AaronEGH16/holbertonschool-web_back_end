#!/usr/bin/env python3
"""
this module contains a simple async function definition
"""

import asyncio
import random
import time

max_delay: int = 10


async def wait_random(wait_time: int =
                      random.randint(0, max_delay)) -> float:
    """
    takes in an integer value and waits its time
    """
    start_time = time.time()
    await asyncio.sleep(wait_time if wait_time in range(0, 11) else 10)
    end_time = time.time()
    return end_time - start_time
