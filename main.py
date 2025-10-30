# Simple Python Program: Add, Subtract, and Multiply Two Numbers

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

def subtract_numbers(a, b):
    """Function to subtract second number from first"""
    return a - b

def multiply_numbers(a, b):
    """Function to multiply two numbers"""
    return a * b

# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform calculations
sum_result = add_numbers(num1, num2)
sub_result = subtract_numbers(num1, num2)
mul_result = multiply_numbers(num1, num2)

# Print results
print("The sum of", num1, "and", num2, "is:", sum_result)
print("The subtraction of", num2, "from", num1, "is:", sub_result)
print("The multiplication of", num1, "and", num2, "is:", mul_result)
