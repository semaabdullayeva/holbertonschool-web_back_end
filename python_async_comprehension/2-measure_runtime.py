#!/usr/bin/env python3
import asyncio
import time

"""Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself. """


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions """
    start_time = time.time()
    tasks = []
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time
