#Write a Python script to sort (ascending and descending) a dictionary by value.

# Sample dictionary
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Sort dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print sorted dictionaries
print()
print("Ascending order:", sorted_dict_asc)
print()
print("Descending order:", sorted_dict_desc)
print()