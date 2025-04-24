#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine and measure_time
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
"""
Importing the wait_n function from another module to use in measure_time.
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n.
    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time per execution.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
