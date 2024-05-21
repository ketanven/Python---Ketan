# Write a Python program to print all unique values in a dictionary.


# Define the dictionary
dict = {1: 'Ketan', 2: 'Pillai', 3: 'Uday', 3: 'Rajput', 4: 'Jay'}

# Initialize a set to store unique values
unique = set()

# Iterate over the values of the dictionary and add them to the set
for i in dict.values():
    unique.add(i)

# Print the unique values
print("Unique Values:", unique)
