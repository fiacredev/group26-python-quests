# Quest 27: The FizzBuzz Test
# Print numbers 1 to 100; Fizz for multiples of 3, Buzz for 5, FizzBuzz for both.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
