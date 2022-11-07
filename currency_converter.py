import requests

my_curr = input().lower()
json_dict = requests.get(f'http://www.floatrates.com/daily/{my_curr}.json').json()
cache = []

if my_curr != 'eur':
    eur = json_dict['eur']['rate']
    cache.append('eur')
if my_curr != 'usd':
    usd = json_dict['usd']['rate']
    cache.append('usd')


def calculate_result(curr, amt):
    ex_rate = json_dict[f'{curr}']['rate']
    res = round((ex_rate * amt), 2)
    return res


while True:
    currency = input().lower()

    if currency == "":
        break
    else:
        amount = float(input())
        print("Checking the cache...")

        if currency in cache:
            print("Oh! It is in the cache!")
            result = calculate_result(currency, amount)
            print(f"You received {result} {currency.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            cache.append(currency)
            result = calculate_result(currency, amount)
            print(f"You received {result} {currency.upper()}.")
