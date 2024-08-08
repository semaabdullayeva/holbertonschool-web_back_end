#!/usr/bin/env python3
import asyncio
import time

async_comprehension=__import__("1-async_comprehension").async_comprehension
async def measure_runtime()->float:
    start_time=time.time()
    tasks=[]
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    asyncio.gather(*tasks)
    
    end_time=time.time()
    return (end_time-start_time)