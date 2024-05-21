# Write a Python function that takes two lists and returns true if they have at least one common member.

def check(list1, list2):
    # Convert list1 to a set to efficiently check for common elements
    set1 = set(list1)
    
    # Iterate through elements in list2
    for element in list2:
        # Check if the current element from list2 exists in set1
        if element in set1:
            # If a common element is found, print a message and return True
            print("YES!! SOME OF ELEMENTS ARE SAME IN BOTH THE LISTS")
            return True
    
    # If no common element is found after checking all elements in list2, return False
    return False

# Define two lists
list1 = [22, 33, 44, 55, "ketan", "pillai", 22, 66]
list2 = [22, 33, 77, 67, 34, 23, 45, 67, 78, 87, 76, 65]

# list2 = [77,88,99,999,89,89,89] //output = false


# Call the check function with the two lists and print the result
print(check(list1, list2))







