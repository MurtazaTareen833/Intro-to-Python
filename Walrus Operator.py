# Example 1: Basic usage
x = 10
if (n := len(str(x))) > 5:
    print(f"The number has more than 5 digits: {n}")
else:
    print(f"The number has {n} digits")

# Example 2: Loop termination condition
while (input_str := input("Enter a value (or 'quit' to exit): ")) != 'quit':
    print(f"You entered: {input_str}")
