# Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string


# Input string
s = input("Enter a string: ")

# Replacing 'not'...'poor' with 'good' if condition met
if 'not' in s and 'poor' in s:
    s = s.replace(s[s.find('not'):s.find('poor')+4], 'good')

# Displaying the resulting string
print("Resulting string:", s)
