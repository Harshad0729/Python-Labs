# WAP to print triangular  pattern
'''
*                         1                         1

* *                       1 2                       2 2 

* * *                     1 2 3                     3 3 3

* * * *                   1 2 3 4                   4 4 4 4
'''

rows = 4  # Number of rows

for i in range(1, rows + 1):
    # Pattern 1: Asterisks (*)
    for _ in range(i):
        print("*", end=" ")
    print(" " * (rows - i) * 2, end="\t")  # Add spaces to align with the next column
    # Pattern 2: Sequential numbers (1 2 3 ...)
    for j in range(1, i + 1):
        print(j, end=" ")
    print(" " * (rows - i) * 2, end="\t")  # Add spaces to align with the last column
    
    # Pattern 3: Repeating numbers (e.g., 1 1, 2 2 2, ...)
    for _ in range(i):
        print(i, end=" ")
    
    # Move to the next line
    print()
