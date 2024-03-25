import argparse

def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

def subtract_numbers(num1, num2):
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")

def multiply_numbers(num1, num2):
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")

def divide_numbers(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The division of {num1} by {num2} is: {result}")

def main():
    parser = argparse.ArgumentParser(description="Basic Calculator")

    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    args = parser.parse_args()

    if args.operation == "add":
        add_numbers(args.num1, args.num2)
    elif args.operation == "subtract":
        subtract_numbers(args.num1, args.num2)
    elif args.operation == "multiply":
        multiply_numbers(args.num1, args.num2)
    elif args.operation == "divide":
        divide_numbers(args.num1, args.num2)

if __name__ == "__main__":
    main()
