#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers with async comprehension
"""
async_generator = __import__('0-async_generator').async_generator
"""
Import async_generator from the previous task
"""


async def async_comprehension():
    """
    Collect 10 random numbers from async_generator and return them
    """
    return [i async for i in async_generator()]
