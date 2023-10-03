"""
Description: Interest Update
Author: Armanjot Kaur
Date: 29 September 2023
Usage: For the Updation of bank's interest
"""
import csv
import pprint
from datetime import datetime


account_balances = {}
with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, balance = line.strip().split("|")
        account_balances[account_number]= float(balance)

pprint.pprint(account_balances)

# calculation of Monthly Interest
for account_number, balance in account_balances.items():
    if balance > 0:
        if balance < 1000:
            interest_rate = 0.01
        elif balance < 5000:
            interest_rate = 0.025
        else: 
            interest_rate = 0.05    

        # Monthly Interest
        monthly_interest = (balance * interest_rate) / 12

        # Balance Updation Include Interest
        account_balances[account_number] += monthly_interest
    elif balance < 0:
        interest_rate = 0.10

        # Monthly Interest Charge
        monthly_interest = (balance * interest_rate) / 12

        # Updation of Balance with Interest Charge
        account_balances[account_number] += monthly_interest

# Display of updated account balances
pprint.pprint(account_balances)







