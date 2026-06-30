# Quest 26: The Simple Calculator
# Ask for two numbers and an operation, then call the matching function.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter an operation (add, subtract, multiply, divide): ").strip().lower()

if operation == "add":
    result = add(first_number, second_number)
elif operation == "subtract":
    result = subtract(first_number, second_number)
elif operation == "multiply":
    result = multiply(first_number, second_number)
elif operation == "divide":
    if second_number == 0:
        print("Cannot divide by zero.")
        exit()
    result = divide(first_number, second_number)
else:
    print("Unknown operation. Use add, subtract, multiply, or divide.")
    exit()

print(f"Result: {result}")
