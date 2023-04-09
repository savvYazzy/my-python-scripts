# Basic calculator script in Python

# Prompt the user for the first number
num1 = float(input("Enter the first number: "))

# Prompt the user for the second number
num2 = float(input("Enter the second number: "))

# Prompt the user for the operator to use
op = input("Enter the operator (+, -, *, /): ")

# Perform the calculation based on the operator
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Invalid operator entered!")
    exit()

# Print the result to the terminal
print("Result: ", result)
