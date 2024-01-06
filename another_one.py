import time, asyncio as asyc
import requests as rq
import aiohttp as asycHttp

import asyncio

# Asynchronous function 1
async def task_one():
    print("Task One started")
    await asyncio.sleep(0.5)  # Simulate an I/O-bound operation
    print("Task One completed")

# Asynchronous function 2
async def task_two():
    print("Task Two started")
    await asyncio.sleep(5)  # Simulate an I/O-bound operation
    print("Task Two completed")

# Asynchronous function 3
async def task_three():
    print("Task Three started")
    await asyncio.sleep(15)  # Simulate an I/O-bound operation
    print("Task Three completed")

async def all_other_tasks():
    await asyncio.sleep(2)
    print("A task was finished")
    await asyncio.sleep(2)
    print("A task was finished")
    await asyncio.sleep(2)
    print("A task was finished")


# Main function to run asynchronous tasks
async def main():
    print("Main function started")

    # Run coroutines concurrently using asyncio.gather()
    await asyncio.gather(task_one(), task_two(), task_three(), all_other_tasks())

    print("All tasks completed")

# Use asyncio.run() to execute the asyncio event loop
asyncio.run(main())


