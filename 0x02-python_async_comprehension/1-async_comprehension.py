#!/usr/bin/env python3

"""
Module: async_comprehension

This module provides a coroutine that collects 10 random numbers
using async comprehension.
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    # Collect 10 random numbers using async comprehension
    return [random_number async for random_number in async_generator()]
