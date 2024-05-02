print()
# Input string
inputstr = input("**ENTER A STRING =  ")
print()

# Check if the length of the string is at least 3 and ends with 'ing'
if len(inputstr) >= 3 and inputstr.endswith('ing'):
    # If yes, append 'ly' to the string
    modified_string = inputstr + 'ly'
else:
    # Otherwise, append 'ing' to the string
    modified_string = inputstr + 'ing'

# Output the modified string
print("---MODIFIED STRING = ", modified_string)
print()
