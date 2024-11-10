# Get user input for the number
num = int(input("Enter a number to calculate the sum of its digits: "))  # Convert input to an integer

# Use absolute value to handle negative numbers
num = abs(num)

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Use a while loop to calculate the sum of digits
while num > 0:
    sum_of_digits += num % 10  # Add the last digit to the sum
    num //= 10  # Remove the last digit from the number

# Print the total sum of digits
print("The sum of the digits is:", sum_of_digits)