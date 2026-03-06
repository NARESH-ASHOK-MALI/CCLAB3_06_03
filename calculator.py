#Building Calculator using Python

operations = {
    '1': ('+', lambda x, y: x + y),
    '2': ('-', lambda x, y: x - y),
    '3': ('*', lambda x, y: x * y),
    '4': ('/', lambda x, y: "Error: Division by zero is not allowed." if y == 0 else x / y),
}

print("Select operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice == '5':
        print("Exiting.")
        break
    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        symbol, func = operations[choice]
        print(f"{num1} {symbol} {num2} = {func(num1, num2)}")
        break
    print("Invalid Input")
