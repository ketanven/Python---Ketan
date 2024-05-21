# # Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# 300}, o {'item': 'item1', 'amount': 750}]
# Expected Output:
# Counter ({'item1': 1150, 'item2': 300})


# Sample data
list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Combine values
combine = {}

for i in list:
    item = i['item']
    amount = i['amount']
    if item in combine:
        combine[item] += amount
    else:
        combine[item] = amount

# Print the combined values
print("Combined values:")
print(combine)
