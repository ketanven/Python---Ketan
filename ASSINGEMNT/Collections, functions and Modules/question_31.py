# Write a Python script to merge two Python dictionaries

# Sample dictionaries
dict1 = {1: 'Ketan', 2: 'Pillai'}
dict2 = {3: 'Uday', 4: 'Rajput'}

# Create a new dictionary to hold the merged result
merged_dict = dict1.copy()  # Start with a copy of the first dictionary
merged_dict.update(dict2)   # Update it with the contents of the second dictionary

# Print the merged dictionary
print()
print("Merged Dictionary:", merged_dict)
print()

