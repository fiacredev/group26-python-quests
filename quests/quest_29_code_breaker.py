secret_code = 42
attempts = 3

print("Welcome! You have 3 attempts to guess the secret code.")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == secret_code:
        print("Correct! You cracked the code!")
        break
    elif guess < secret_code:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Out of attempts! The secret code was {secret_code}.")