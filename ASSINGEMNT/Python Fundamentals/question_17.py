# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string

# Input strings
input1 = input("Enter the first string: ")
input2 = input("Enter the second string: ")

# Swapping the first two characters
newstring1 = input2[:2] + input1[2:]
newstring2 = input1[:2] + input2[2:]

# Concatenating the strings with a space
output = newstring1 + ' ' + newstring2

# Displaying the result
print("Result:", output)
