# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.


print()
# Input string
inputstr = input("**ENTER A STRING =  ")
print()

# Check if the length of the string is at least 3 and ends with 'ing'
if len(inputstr) >= 3 and inputstr.endswith('ing'):
    # If yes, append 'ly' to the string
    modifiedstring = inputstr + 'ly'
else:
    # Otherwise, append 'ing' to the string
    modifiedstring = inputstr + 'ing'

# Output the modified string
print("---MODIFIED STRING = ", modifiedstring)
print()
