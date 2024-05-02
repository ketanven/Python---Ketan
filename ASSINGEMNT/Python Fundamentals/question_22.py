# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string3



# Input string
given_string = input("Enter a string: ")

# Check if the length of the string is less than 2
if len(given_string) < 2:
    result = ""
else:
    # Get the first 2 and last 2 characters
    result = given_string[:2] + given_string[-2:]

# Display the result
print("Resulting string:", result)
