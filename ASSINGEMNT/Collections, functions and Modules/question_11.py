#Write a Python program to get unique values from a list

# List with duplicate values
list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 10, 10]

# Create an empty list to store unique values
uniquelist = []

# Iterate through the input list
for value in list:
    # If the value is not already in the unique_list, add it
    if value not in uniquelist:
        uniquelist.append(value)

# Print the original and the list with unique values
print()
print("Original list:", list)
print()
print("List of unique values:", uniquelist)
print()
