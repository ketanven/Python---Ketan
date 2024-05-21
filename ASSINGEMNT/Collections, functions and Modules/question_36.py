# Write a Python program to find the highest 3 values in a dictionary


# Sample dictionary
my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

# Get the values from the dictionary
values = list(my_dict.values())

# Sort the values in descending order
values.sort(reverse=True)

# Get the highest 3 values
highest_values = values[:3]

# Find the keys corresponding to the highest values
highest_keys = [key for key, value in my_dict.items() if value in highest_values]

# Print the highest 3 values and their keys
print("Highest 3 values in the dictionary:")
for key, value in zip(highest_keys, highest_values):
    print(key, "=", value)
