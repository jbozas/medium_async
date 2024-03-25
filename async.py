from decimal import Decimal
import asyncio
import aiohttp
from time_it import time_it
import random


async def fetch_api(currency_to: str) -> dict:
    url = f"https://economia.awesomeapi.com.br/{currency_to}/1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()


async def main() -> None:
    """
    Makes a conversion between ARG currency and
    USD currency.
    """
    for _ in range(100):
        currency_to = "USD-ARS"
        amount = random.randint(10, 99999)
        response = await fetch_api(currency_to)
        change = Decimal(response[0].get("high"))
        print(f"With {amount} dollars you will get {change*amount} Argentine pesos")


@time_it
def call_async_main():
    asyncio.run(main())


if __name__ == "__main__":
    call_async_main()
