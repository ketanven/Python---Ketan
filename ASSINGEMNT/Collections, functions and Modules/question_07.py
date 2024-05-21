#Write a Python function that takes a list and returns a new list with unique
#elements of the first list.


# Original list with duplicate elements
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 10, 10]

# Create an empty list to store unique elements
unique_list = []

# Iterate through the original list
for i in original_list:
    # If the element is not already in the unique_list, add it
    if i not in unique_list:
        unique_list.append(i)

# Print the original and the list with unique elements
print()
print("Original list:", original_list)
print()
print("Unique elements list:", unique_list)
print()
