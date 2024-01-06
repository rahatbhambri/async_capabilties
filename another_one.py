import time, asyncio as asyc
import requests as rq
import aiohttp as asycHttp
import asyncio


# Asynchronous function 1
async def task_one():
    print("Task One started")
    res = rq.get("https://www.google.com")
    print(str(res.text)[:50])
    res = rq.get("https://www.google.com")
    print(str(res.text)[:50])
    await asyncio.sleep(15)
    res = rq.get("https://www.google.com")
    print(str(res.text)[:50])
    res = rq.get("https://www.google.com")
    print(str(res.text)[:50])
    print("Task One completed")

# Asynchronous function 2
async def task_two():
    print("Task Two started")
    res = rq.get("https://www.facebook.com")
    print(str(res.text)[:50])
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
    print("Other tasks completed")


# Main function to run asynchronous tasks
async def main():
    print("Main function started")

    # Run coroutines concurrently using asyncio.gather()
    await asyncio.gather( task_one(), task_three(), all_other_tasks())


# Use asyncio.run() to execute the asyncio event loop
asyncio.run(main())


