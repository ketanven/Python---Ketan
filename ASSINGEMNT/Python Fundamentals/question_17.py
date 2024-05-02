# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string

# Input strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swapping the first two characters
new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

# Concatenating the strings with a space
result = new_string1 + ' ' + new_string2

# Displaying the result
print("Result:", result)
