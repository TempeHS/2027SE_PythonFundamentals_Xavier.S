import sys
import requests


def main():
    # 1) Check command-line argument exists
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # 2) Convert argument to a number (bitcoin amount)
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 3) Get current bitcoin price in USD from API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        sys.exit("Request failed")

    # 4) Extract USD price and do conversion
    usd_price = data["bpi"]["USD"]["rate_float"]
    total_cost = bitcoin_amount * usd_price

    # 5) Print formatted USD amount
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
