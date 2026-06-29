#Assignment 1: number guesing game

import random

secret = random.randint(1, 10) # picks a random number

guess = int(input("Guess a number between 1 and 10: ")) # gets input from user and converts to integer

if guess == secret:
    print("You got it!")
else:
    print(f"Nope! It was {secret}.") # shows the answer if wrong


#Assignment 2: choose your own adventure

def start():
    print("You wake up in a forest. Two paths lie ahead.")
    print("Type left or right")
    choice = input("> ")

    if choice == "left":
        cave() # goes to cave funtion
    elif choice == "right":
        river()
    else:
        print("thats not valid")

def cave():
    print("You find a chest. Open it or leave?")
    choice = input("> ")

    if choice == "open":
        ending_good()
    elif choice == "leave":
        ending_bad() # bad ending if they leave
    else:
        print("invalid")

def river():
    print("Theres a boat. Take it or swim?")
    choice = input("> ")

    if choice == "take":
        ending_good()
    elif choice == "swim":
        ending_bad()
    else:
        print("invalid")

def ending_good():
    print("You made it home. YOU WIN!")

def ending_bad():
    print("You got lost. GAME OVER.")

start() # runs the game


#Assignment 3: code breaker

secret_code = 42 # the code they have to guess
attempts = 3 # only 3 tries

print("You have 3 attempts to guess the secret code.")

for i in range(attempts): # loops 3 times
    guess = int(input("Enter your guess: "))

    if guess == secret_code:
        print("Correct!")
        break # stops if they get it right
    elif guess < secret_code:
        print("Too low!")
    else:
        print("Too high!")
else:
    # this runs only if they never guessed right
    print(f"Out of attempts. The code was {secret_code}.")