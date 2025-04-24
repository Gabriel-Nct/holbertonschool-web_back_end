#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine and that waits for
a random delay between 0 and max_delay
"""
import random
import asyncio
"""
an asynchronous coroutine and that waits for
a random delay between 0 and max_delay
"""


async def wait_random(max_delay: int = 10):
    """
    an asynchronous coroutine and that waits for
    a random delay between 0 and max_delay
    Args:
    max_delay: an integer
    Returns:
    The delay waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
