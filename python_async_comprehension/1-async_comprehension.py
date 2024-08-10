#!/usr/bin/env python3
<<<<<<< HEAD
""" Import async_generator from the previous task and then write a coroutine
    called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers. """
=======
"""Async Comprehensions"""
>>>>>>> 0b7ffa6a26dd32da935a7b24a84d424baca598b7
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
<<<<<<< HEAD
    """ Async Comprehensions """
=======
    """The coroutine will collect 10 random numbers using
        an async comprehensing over async_generator, then
        return the 10 random numbers. """
>>>>>>> 0b7ffa6a26dd32da935a7b24a84d424baca598b7
    return [i async for i in async_generator()]
