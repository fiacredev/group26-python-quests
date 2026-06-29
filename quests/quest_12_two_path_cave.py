#!/usr/bin/python3
# Quest 12: The Two-Path Cave
# Password checker: grant or deny access.

secret_password = "open-sesame"

entered_password = input("Speak the secret password: ")

if entered_password == secret_password:
    print("Access Granted")
else:
    print("Access Denied")
