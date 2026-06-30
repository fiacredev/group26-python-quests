secret_number = 7

guess = int(input("Guess the secret number: "))

while guess != secret_number:
    print("Wrong! Try again.")
    guess = int(input("Guess the secret number: "))

print("Congratulations! You guessed it!")
