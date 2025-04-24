#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine and that waits for
a random delay between 0 and max_delay
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
"""
Importing the wait_random function from another module to use in wait_n.
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): the number of concurrent executions we want to perform.
        max_delay (int): the maximum delay we allow
        for each wait_random execution.

    Returns:
        List[float]: a list of float values representing the delays.
    """

    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = []

    for task in tasks:
        delay = await task
        index = 0
        while index < len(delays) and delays[index] < delay:
            index += 1
        delays.insert(index, delay)

    return delays
