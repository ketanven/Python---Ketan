# Write a Python script to concatenate following dictionaries to create a new one.

# Define the dictionaries
dict1 = {1: 'ketan', 2: 'Uday', 3: 'Jay'}
dict2 = {4: 'Python', 5: 'Django', 6: 'C++'}

# Create a new dictionary by copying dict1
new_dict = dict1.copy()

# Update the new dictionary with the contents of dict2
new_dict.update(dict2)

# Print the new concatenated dictionary
print()
print("Concatenated Dictionary:", new_dict)
print()
