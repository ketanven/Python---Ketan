# Write a Python program to find the highest 3 values in a dictionary

# Sample dictionary
mydict = {1: "ketan", 2: "Uday", 3: "Pillai", 4: "Rajput", 5: "Raj"}

# Function to get the value for sorting
def value(item):
    return item[1]

# Sort the dictionary items by value in descending order using the custom function
sorted = sorted(mydict.items(), key=value, reverse=True)

# Get the highest 3 items
highest = sorted[:3]

# Print the highest 3 values and their keys
print("Highest 3 values in the dictionary:")
for i, j in highest:
    print(i, "=", j)

