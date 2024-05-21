# Write a Python program to check a list is empty or not


def empty(list):
    # Check if the list is empty
    if not list:
        # If the list is empty, return True
        return True
    else:
        # If the list is not empty, return False
        return False

# Example usage:
checklist = []
if empty(checklist):
    # If the list is empty, print a message indicating it's empty
    print("--THE LIST IS EMPTY :(--")
else:
    # If the list is not empty, print a message indicating it's not empty
    print("--THE LIST IS NOT EMPTY :)--")

