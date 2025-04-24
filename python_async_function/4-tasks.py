#!/usr/bin/env python3
"""Module provides the function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
"""
importing function from task 3
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """executes task_wait_random n
    times and returns lists of delays (sorted)"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)
    return delays
