#!/usr/bin/env python3
"""Async Comprehensions """
import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator

"""The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator, then
    return the 10 random numbers."""


async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]
