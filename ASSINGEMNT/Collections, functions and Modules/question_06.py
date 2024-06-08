# Write a Python program to generate and 
# print a list of first and last 5 elements where the values are square of numbers between 1 and 30.


# Generate a list of squares of numbers between 1 and 30
squares = [i**2 for i in range(1, 31)]

# Get the first 5 elements
first_five = squares[:5]

# Get the last 5 elements
last_five = squares[-5:]

# Print the results
print()
print("First 5 elements:", first_five)
print()
print("Last 5 elements:", last_five)
print()
print(squares)
print()