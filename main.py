# Simple Python Program: Add Two Numbers

def add_numbers(a, b):
    return a + b

# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate sum using function
result = add_numbers(num1, num2)

# Print result
print("The sum of", num1, "and", num2, "is:", result)
