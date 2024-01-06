import time, asyncio as asyc
import requests as rq
import aiohttp as asycHttp


async def waitedCompute(s):
  for i in range(5):
    time.sleep(2)
    yield i * (s)


async def summation():
  session = asycHttp.ClientSession()
  async with session.get("https://www.google.com") as resp:
    it = waitedCompute(str(resp)[:50]).__aiter__()
    try:
      while True:
        s = await it.__anext__()
        print(s)
    except Exception as e:
      print(e, "ascs")


asyc.run(summation())

#new comment 