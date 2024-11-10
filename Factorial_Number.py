# Get user input for the number
number = int(input("Enter a number: "))  # Convert input to an integer

# Initialize factorial variable to 1 (since factorial of 0 is 1 by definition)
factorial = 1

# Initialize a counter variable to the value of the number
counter = number

# Start the while loop to calculate factorial
while counter > 0:
    factorial *= counter  # Multiply factorial by the current counter value
    counter -= 1          # Decrement the counter by 1 in each iteration

# Print the final result
print("The factorial of", number, "is:", factorial)
