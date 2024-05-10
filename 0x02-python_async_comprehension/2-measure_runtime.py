#!/usr/bin/env python3

"""
Module: measure_runtime

This module provides a coroutine to measure the runtime of async_comprehension.
"""

import asyncio
import time
from typing import List


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of async_comprehension executed
    four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """

    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
