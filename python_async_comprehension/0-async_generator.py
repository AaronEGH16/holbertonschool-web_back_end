#!/usr/bin/env python3
"""
this module contains a async function
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    this function generate random number 10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
