# # Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers.


def maxmin(numbers):
    # Find the maximum number in the list
    max_number = max(numbers)
    # Find the minimum number in the list
    min_number = min(numbers)
    # Return the maximum and minimum numbers
    return max_number, min_number

# Test the function with a list of numbers
numbers = [3.14, 2.71, 1.618, 0.577, 4.669]
# Call the function to find the maximum and minimum numbers
max_num, min_num = maxmin(numbers)

# Print the maximum and minimum numbers
print()
print("Maximum number:", max_num)
print()
print("Minimum number:", min_num)

