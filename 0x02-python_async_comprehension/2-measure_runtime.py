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
    # Start measuring the time
    start_time = time.time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Stop measuring the time
    end_time = time.time()

    # Calculate the total runtime
    total_runtime = end_time - start_time

    return total_runtime


async def main() -> None:
    """
    Main function to execute and measure the runtime of async_comprehension.
    """
    total_runtime = await measure_runtime()
    print(f"Total runtime: {total_runtime:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
