#Write a Python program to check multiple keys exists in a dictionary


# Define the dictionary
dict = {1: 'Ketan', 2: 'Pillai', 3: 'Uday', 4: 'Rajput', 5: 'Jay'}

# Keys to check
check = [1, 4, 6]

# Check if each key exists in the dictionary
for key in check:
    if key in dict:
        print()
        print(f"The key '{key}' exists in the dictionary.")
        print()
    else:
        print()
        print(f"The key '{key}' does not exist in the dictionary.")
        print()
