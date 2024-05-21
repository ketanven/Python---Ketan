#Write a Python program to replace last value of tuples in a list.

# List of tuples
tupleslist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(tupleslist)

# New value to replace the last element
newvalue = 10

# Iterate through each tuple in the list
for i in range(len(tupleslist)):
    # Convert the tuple to a list, replace the last element, and convert back to tuple
    tupleslist[i] = tuple(list(tupleslist[i])[:-1] + [newvalue])

# Print the updated list of tuples
print()

print("Updated list of tuples:", tupleslist)
print()
