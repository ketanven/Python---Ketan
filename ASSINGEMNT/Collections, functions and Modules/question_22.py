#Write a Python program to find the repeated items of a tuple.

# Tuple to analyze
my_tuple = (1, 2, 2, 3, 4, 4, 5)

# Find repeated items
repeated_items = frozenset(item for item in my_tuple if my_tuple.count(item) > 1)

# Print the repeated items
print()
print("Repeated items:", repeated_items)
print()
