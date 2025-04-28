#!/usr/bin/env python3
"""
Module to measure the runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
"""
import asyncio, time and async_comprehesion from 1-async_comprehension
"""


async def measure_runtime():
    """
    Measure total runtime of four parallel async_comprehensions
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
