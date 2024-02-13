import asyncio
import aiohttp
import time
import requests


async def AnotherOne(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def getAllDataAsync():
    tasks = [AnotherOne(f"https://dummyjson.com/products/{i}") for i in range(1, 10)]
    results = await asyncio.gather(*tasks)
    for res in results:
        print(res)

def getAllData():
    result = []
    for i in range(1, 10):
        url = f"https://dummyjson.com/products/{i}"
        respo = requests.get(url)
        result.append(respo.json())
    return result

tpc = time.perf_counter()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(getAllDataAsync())

Timeup = time.perf_counter() - tpc
print(f"Executed in {Timeup:0.2f} seconds.")

tpc = time.perf_counter()
print(getAllData())
Timeup = time.perf_counter() - tpc
print(f"Executed in {Timeup:0.2f} seconds.")
