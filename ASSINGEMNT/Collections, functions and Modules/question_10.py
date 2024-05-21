#Write a Python program to find the second smallest number in a list.

# List of numbers
numbers = [12, 5, 7, 1, 18, 9, 3, 15, 8, 4]

# Ensure the list has at least two unique elements
if len(numbers) < 2:
    print("List must have at least two unique elements.")
else:
    # Sort the list and remove duplicates
    unique_numbers = sorted(set(numbers))
    
    # Check if there are at least two unique elements after removing duplicates
    if len(unique_numbers) < 2:
        print("List must have at least two unique elements.")
    else:
        # The second smallest number will be the second element in the sorted unique list
        smallest = unique_numbers[1]
        print("The second smallest number is:", smallest)
