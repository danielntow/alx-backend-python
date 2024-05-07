#!/usr/bin/env python3

"""
Module: async_operations

This module provides asynchronous coroutines for performing
operations with random delays.
"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with
    the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each
        wait_random call.

    Returns:
        List[float]: A list of all the delays (float values)
        in ascending order.
    """
    # Create a list to store the results
    delays = []
    # Create tasks for wait_random and store them in a list
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Wait for all tasks to complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return sorted(delays)  # Sort the delays in ascending order
