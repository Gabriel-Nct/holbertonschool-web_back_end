#!/usr/bin/env python3
"""
This module provides a function
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
"""
Import the wait_random function from the basic_async_syntax module.
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task that runs wait_random with the provided max_delay.
    Args:
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        asyncio.Task: the asyncio.Task created.
    """
    return asyncio.create_task(wait_random(max_delay))
