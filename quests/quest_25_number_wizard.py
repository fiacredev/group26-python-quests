# Quest 25: The Number Wizard
# Guess the secret number; get "too high" or "too low" hints after each wrong guess.

secret = 42

print("I am thinking of a number between 1 and 100.")
print("Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You guessed the number!")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
