# WAP to traverse a list of item and find particular item is present in the list or not.

# List of items
items = [10, 20, 30, 40, 50]

# Input: item to search for
search_item = int(input("Enter the item to search: "))

# Check if item is in the list
found = False
for item in items:
    if item == search_item:
        found = True
        break

# Output the result
if found:
    print("Item found in the list.")
else:
    print("Item not found in the list.")
