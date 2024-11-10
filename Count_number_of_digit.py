# Get user input for the number
num = int(input("Enter a number to count: "))  # Convert input to an integer

# Initialize a variable to count digits
digit_count = 0

# Use a while loop to count the digits
while num > 0:
    num //= 10  # Remove the last digit from the number
    digit_count += 1  # Increment the digit count

# Print the total number of digits
print("The number of digits is:", digit_count)
