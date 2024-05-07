#!/usr/bin/env python3

"""
Module: async_tasks

This module provides functions for creating asyncio Tasks.
"""

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create an asyncio.Task that executes wait_random with
    the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        Task[float]: An asyncio.Task that executes wait_random.
    """
    # Create an asyncio.Task that executes wait_random with the
    # specified max_delay
    task = asyncio.create_task(wait_random(max_delay))
    return task
