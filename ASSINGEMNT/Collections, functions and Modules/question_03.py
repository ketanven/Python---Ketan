# Write a Python program to remove duplicates from a list.

# Define a list with integers and strings
list = [22, 33, 44, 22, 55, 11, 55, 22, 22, 33, 44, "ketan", "ketan"]

# Convert the list to a set to remove duplicates
result1 = set(list)

# Convert the list to a frozenset, which is an immutable version of set
result2 = frozenset(list)

print()
# Print the new list with duplicates removed using set
print("DUPLICATES REMOVED NEW LIST = ", result1)
print()

# Print the new list with duplicates removed using frozenset
print("DUPLICATES REMOVED NEW LIST = ", result2)
print()
