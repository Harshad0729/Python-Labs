# WAP to get factorial of a number

# Program to find the factorial of a number using a for loop

# Input: number to find factorial
num = int(input("Enter a number: "))

# Initializing factorial to 1
factorial = 1

# Calculate factorial using for loop
for i in range(1, num + 1):
    factorial *= i

# Output the result
print(f"The factorial of {num} is {factorial}")
