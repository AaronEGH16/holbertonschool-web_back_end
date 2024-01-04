#!/usr/bin/env python3
"""
this module contains a function definition
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    this function create a async task obj and return it
    """
    return asyncio.create_task(wait_random(max_delay))
