#!/usr/bin/env python3
"""
this module contains an async function definition
"""
import asyncio
from time import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """this async function calculates measure runtime of
    iterated async function"""
    start_time = time()
    runtime_list = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*runtime_list)
    end_time = time()
    return end_time - start_time
