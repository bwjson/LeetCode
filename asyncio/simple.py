import time
import asyncio

async def long_operation():
    print("starting long")
    await asyncio.sleep(1)
    print('success')

async def short_operation():
    print("starting short")
    await asyncio.sleep(3)
    print('unauthorized')

async def main():
    await asyncio.gather(long_operation(), short_operation())

asyncio.run(main())


