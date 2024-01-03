#!/usr/bin/env python3
"""
this module contains a simple async function definition
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes a max_delay integer and wait a random
    time beetween 0 and max_delay
    """
    wait = random.uniform(0, (max_delay if max_delay in range(0, 11) else 10))
    await asyncio.sleep(wait)
    return wait
