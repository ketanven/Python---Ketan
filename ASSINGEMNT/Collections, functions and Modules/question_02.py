# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.



def check(strings):
    # Initialize a counter to keep track of strings where the first and last characters are the same
    count = 0
    # Iterate through each string in the list of strings
    for s in strings:
        # Check if the length of the string is at least 2 characters and if the first and last characters are the same
        if len(s) >= 2 and s[0] == s[-1]:
            # If the conditions are met, increment the count
            count += 1
    # Return the count of strings meeting the criteria
    return count

# Define a list of strings
list = ["abc", "aba", "ketan", "pillai", "uday", "rajput", "222302", "11223344", "task"]

# Call the check function to count the number of strings where the first and last character are the same
print("Number of strings where the first and last character are the same:", check(list))

