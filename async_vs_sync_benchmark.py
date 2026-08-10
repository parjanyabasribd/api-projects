import asyncio
import aiohttp
import requests
import time

currencies = ["BTC", "ETH", "USD"]

def fetch_data_sync(currency):
    url = "https://api.coinbase.com/v2/exchange-rates"
    response = requests.get(url, params={"currency": currency})
    data = response.json()
    print(f"Currency: {currency}, Rate to USD: {data['data']['rates']['USD']}")

def main_sync():
    for currency in currencies:
        fetch_data_sync(currency)

async def fetch_data_async(session, currency):
    url = "https://api.coinbase.com/v2/exchange-rates"
    async with session.get(url, params={"currency": currency}) as response:
        data = await response.json()
        print(f"Currency: {currency}, Rate to USD: {data['data']['rates']['USD']}")

async def main_async():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(fetch_data_async(session, c) for c in currencies))

if __name__ == "__main__":
    st = time.perf_counter()
    main_sync()
    sync_time = time.perf_counter() - st
    print(f"Executed in {sync_time:.2f} seconds using sync.\n")

    st = time.perf_counter()
    asyncio.run(main_async())
    async_time = time.perf_counter() - st
    print(f"Executed in {async_time:.2f} seconds using async.")
    print(f"Async was {sync_time/async_time:.2f}x faster")