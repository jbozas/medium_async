from decimal import Decimal
import requests
from time_it import time_it
import random


def fetch_api(currency: str) -> dict:
    url = f"https://economia.awesomeapi.com.br/{currency}/1"
    return requests.get(url).json()


@time_it
def main() -> None:
    """
    Makes a conversion between ARG currency and
    USD currency.
    """
    for _ in range(100):
        currency_to = "USD-ARS"
        amount = random.randint(10, 99999)
        response = fetch_api(currency_to)
        change = Decimal(response[0].get("high"))
        print(f"With {amount} dollars you will get {change*amount} Argentine pesos")


if __name__ == "__main__":
    main()
