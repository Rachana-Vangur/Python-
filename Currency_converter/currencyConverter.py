import os
import subprocess
import sys

import requests

# def install(package):
#     subprocess.call([sys.executable, "-m", "pip", "install", package])


def converter(fromCurr, toCurr, amount):

    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    currencies = data["rates"]
    if fromCurr != "IND":
        amount = amount / currencies[fromCurr]
    result = round(amount * currencies[toCurr], 2)

    return result


def currenyConverter():
    # install(requests)
    os.system("pip install requests:")
    fromCurr = input("From currency: ")
    toCurr = input("To currency: ")
    amount = int(input("Amount: "))
    print(converter(fromCurr, toCurr, amount))


currenyConverter()
# import forex_python
# from datetime import datetime
#
# import requests
# from forex_python.converter import CurrencyRates
#
#
# def exchange_rates(fromCurr, toCurr, time):
#     c = CurrencyRates()
#     print(c.get_rate(fromCurr, toCurr, time))
#     return
#
#
# def convert(fromCurr, toCurr, amount):
#     rate = exchange_rates(fromCurr, toCurr, datetime.now())
#     result = rate * amount
#     return result
#
#
# def currency_Converter():
#
#     fromCountry = input("From Currency: ")
#     toCountry = input("To Currency: ")
#     amount = input("Amount: ")
#     converted_amount = convert(fromCountry, toCountry, amount)
#     print(converted_amount)
#
#
# currency_Converter()
