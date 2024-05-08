# Write a Python program to check a list is empty or not


def empty(list):
    if not list:
        return True
    else:
        return False

# Example usage:
checklist = []
if empty(checklist):
    print("--THE LIST IS EMPTY :(--")
else:
    print("--THE LIST IS NOT EMPTY :)--")
