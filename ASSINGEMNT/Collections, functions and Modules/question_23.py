# Write a Python program to remove an empty tuple(s) from a list of tuples.

# List of tuples
tupleslist = [(1, 2), (), (3, 4), (), (5, 6)]

# Remove empty tuples using a simple loop
remove = []
for t in tupleslist:
    if t:
        remove.append(t)

# Print the filtered list
print()
print("List after removing empty tuples:", remove)
print()
