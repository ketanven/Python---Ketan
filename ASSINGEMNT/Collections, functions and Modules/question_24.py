#Write a Python program to unzip a list of tuples into individual lists.

# List of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Unzip the list of tuples into individual lists
list1, list2 = zip(*tuples_list)

# Convert the result from tuples to lists
list1 = list(list1)
list2 = list(list2)

# Print the individual lists
print()
print("List 1:", list1)
print()
print("List 2:", list2)
print()