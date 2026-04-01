import requests
import sys




def stage1():
    mycoins = float(input("Please, enter the number of mycoins you have: > "))
    rate = float(input("Please, enter the exchange rate: > "))
    result = round(mycoins * rate, 2)
    print(f"The total amount of dollars: {result}")




def stage2():
    rates = {
        "ARS": 0.82,
        "HNL": 0.17,
        "AUD": 1.9622,
        "MAD": 0.208,
    }
    amount = float(input("> "))
    for currency, rate in rates.items():
        result = round(amount * rate, 2)
        print(f"I will get {result} {currency} from the sale of {amount} mycoins.")




def stage3():
    currency_code = input("> ").strip().lower()
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response = requests.get(url, timeout=10)
    data = response.json()

    usd = data.get("usd")
    eur = data.get("eur")

    if usd:
        print(f"1 {currency_code.upper()} = {usd['rate']} USD")
    if eur:
        print(f"1 {currency_code.upper()} = {eur['rate']} EUR")




def stage4():
    base_currency = input("> ").strip().lower()

    # Fetch all rates for base currency
    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    response = requests.get(url, timeout=10)
    all_rates = response.json()

    # Pre-cache USD and EUR
    cache = {}
    if "usd" in all_rates:
        cache["usd"] = all_rates["usd"]["rate"]
    if "eur" in all_rates:
        cache["eur"] = all_rates["eur"]["rate"]

    while True:
        target = input("> ").strip().lower()
        if not target:
            break
        amount = float(input("> ").strip())

        print("Checking the cache...")
        if target in cache:
            print("It is in the cache!")
            rate = cache[target]
        else:
            print("Sorry, but it is not in the cache!")
            if target in all_rates:
                rate = all_rates[target]["rate"]
            else:
                # fetch fresh
                t_url = f"http://www.floatrates.com/daily/{base_currency}.json"
                t_response = requests.get(t_url, timeout=10)
                t_data = t_response.json()
                rate = t_data[target]["rate"]
            cache[target] = rate

        result = round(amount * rate, 2)
        print(f"You received {result} {target.upper()}.")




if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "4"
    stages = {"1": stage1, "2": stage2, "3": stage3, "4": stage4}
    stages.get(stage, stage4)()
