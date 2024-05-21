# # Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers.


def find_max_min(numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    return max_number, min_number

# Test the function 
numbers = [3.14, 2.71, 1.618, 0.577, 4.669]
max_num, min_num = find_max_min(numbers)

# Print the results
print("Maximum number:", max_num)
print("Minimum number:", min_num)
