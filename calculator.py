import math

def calculator():
    print("Welcome to the Scientific Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Tangent (tan)")
    print("8. Square Root (sqrt)")
    print("9. Power (^)")

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

    def sine(x):
        return math.sin(math.radians(x))

    def cosine(x):
        return math.cos(math.radians(x))

    def tangent(x):
        return math.tan(math.radians(x))

    def square_root(x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return "Error: Square root of a negative number is not allowed."

    def power(base, exponent):
        return math.pow(base, exponent)

    while True:
        choice = input("Enter the number of the operation you'd like to perform (or 'q' to quit): ")
        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            match choice:
                case '1':
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                case '2':
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                case '3':
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                case '4':
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                case '5':
                    num = float(input("Enter the number (in degrees): "))
                    print(f"Result: sin({num}) = {sine(num)}")
                case '6':
                    num = float(input("Enter the number (in degrees): "))
                    print(f"Result: cos({num}) = {cosine(num)}")
                case '7':
                    num = float(input("Enter the number (in degrees): "))
                    print(f"Result: tan({num}) = {tangent(num)}")
                case '8':
                    num = float(input("Enter the number: "))
                    print(f"Result: sqrt({num}) = {square_root(num)}")
                case '9':
                    base = float(input("Enter the base number: "))
                    exponent = float(input("Enter the exponent: "))
                    print(f"Result: {base}^{exponent} = {power(base, exponent)}")
                case _:
                    print("Invalid choice. Please select a valid operation.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
