"""
Description: Transactions of Pixell Bank
Author: Armanjot Kaur
Date : 29 September 2023
Usage: use for creating Pixell bank transactions
"""

#  Transaction options
import random
import locale
options = ["D", "W", "Q"]

initial_balance = round(random.uniform(-1000, 10000), 2)
locale.setlocale(locale.LC_ALL, '')
print("*" * 40)
print("PIXELL RIVER FINANCIAL" .center(40))
print("ATM Simulator" .center(40))
print(f"Your current balance is: {locale.currency(initial_balance)}".center(40))
print()
print("Deposit: D" .center(40))
print("Withdraw: W" .center(40))
print("To Quit: Q".center(40))
print("*" * 40)


## Incorporate Transactions of ATM

while True:
    selection = input("Enter your selection: ").upper()

    if selection not in options:
        print("*" * 40)
        print("INVALID SELECTION".center(40))
        print("*" *40)

    else:
        if selection == "Q" :
            break 
        elif  selection == "D":
            deposit_amount = float(input("Enter amount of transaction:"))
            initial_balance += deposit_amount
            print(f"Your Current Balance is: {initial_balance:.2f}")
        elif selection == "W":
            withdraw_amount = float(input("Enter amount of transaction"))
            if withdraw_amount <= initial_balance:
                initial_balance -= withdraw_amount
                print("*" * 40)
                print("*" *40)
                print(f"Your Current Balance is: {initial_balance:.2f}")
                print("*" *40)

# Multiple Transactions    

import os
from time import sleep
while True:
    Selection = input("Enter your selection:").upper()

    if selection not in options:
        print("*" * 40)
        print("INVALID SELECTION".center(40))
        print("*" * 40)
    else:
        if selection == "Q":
            break
        if selection == "D":
            deposit_amount = float(input("Enter amount of transaction:"))
            initial_balance += deposit_amount
            print(f"Your Current Balance is: {initial_balance:2f}")
        elif selection =="W":
            withdraw_amount = float(input("Enter amount of transaction: "))
            if withdraw_amount <= initial_balance:
                initial_balance -= withdraw_amount
                print("*" * 40)
                print("*" * 40)
                print(f"Your Current Balance is : {initial_balance:.2f}")
        else:
            print("*" * 40)
            print("Insufficient Funds".center(40))
sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')








 







