#Write a Python script to sort (ascending and descending) a dictionary by value.

# Sample dictionary
my_dict = {1: "Ketan", 2: "Uday", 3: "Rajput",4:"Pillai"}

# Function to get the value for sorting
def get_value(item):
    return item[1]

# Sort dictionary by value in ascending order
sorted_items_asc = sorted(my_dict.items(), key=get_value)
sorted_dict_asc = dict(sorted_items_asc)

# Sort dictionary by value in descending order
sorted_items_desc = sorted(my_dict.items(), key=get_value, reverse=True)
sorted_dict_desc = dict(sorted_items_desc)

# Print sorted dictionaries
print("Ascending order:", sorted_dict_asc)
print("Descending order:", sorted_dict_desc)
