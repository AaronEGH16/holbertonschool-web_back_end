#!/usr/bin/env python3
"""
this module contains an async function definition
"""
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """this async function calculates measure runtime of
    iterated async function"""
    runtime_list = [async_comprehension() for _ in range(4)]
    executed = await asyncio.gather(*runtime_list)
    for x in range(4):
        executed[x] = sum(executed[x]) / len(executed[x])
    return sum(executed) / len(executed)
