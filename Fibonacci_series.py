# Get user input for the number of terms in the Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))

# Initialize the first two Fibonacci numbers and a counter
a, b = 0, 1  # a is the first term, b is the second term
count = 0    # Counter for the number of terms printed

# Print the Fibonacci series up to n terms
while count < n:
    print(a, end=' ')  # Print the current term
    # Update the values for the next term
    a, b = b, a + b    # a takes the value of b, b takes the value of a + b
    count += 1         # Increment the counter


