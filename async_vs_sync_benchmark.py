import time
import random

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# synchronization/sequential execution
def main_sync():
    for name in names:
        fetch_data_sync(name)

def fetch_data_sync(x):
    delay = random.uniform(0.5, 3.0)
    print(f"Initiating data fetch for Name:{x}...")
    time.sleep(delay)
    print(f"Data fetch completed for Name:{x} after {delay:0.2f} seconds")


# asynchronization/concurrent execution
import asyncio

async def main_async():
    await asyncio.gather(*(fetch_data_async(name) for name in names))

async def fetch_data_async(x):
    delay = random.uniform(0.5, 3.0)
    print(f"Initiating data fetch for Name:{x}...")
    await asyncio.sleep(delay)
    print(f"Data fetch completed for Name:{x} after {delay:0.2f} seconds")


if __name__ == "__main__":
    st = time.perf_counter()
    main_sync()
    end = time.perf_counter()
    sync_time = end - st
    print(f"Executed in {sync_time:0.2f} seconds using sync.")

    st = time.perf_counter()
    asyncio.run(main_async())
    end = time.perf_counter()
    async_time = end - st
    print(f"Executed in {async_time:0.2f} seconds using async.")
    print(f"Async execution was {sync_time/async_time:0.2f} times faster")