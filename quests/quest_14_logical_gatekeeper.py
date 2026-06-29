#!/usr/bin/python3
# Quest 14: The Logical Gatekeeper
# Enter only if 18+ AND have 20+ gold.

age = int(input("How old are you? "))
gold = int(input("How many gold coins do you have? "))

if age >= 18 and gold >= 20:
    print("Welcome to the club! Enjoy your night.")
else:
    print("Sorry, you cannot enter. You need to be 18+ and have 20+ gold coins.")
