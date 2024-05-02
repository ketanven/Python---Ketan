# Write a Python program to count the number of characters (character
# frequency) in a string


# Input string
input_string = input("Enter a string: ")

# Dictionary to store character frequencies
dist = {}

# Counting characters
for char in input_string:
    if char in dist:
        dist[char] += 1
    else:
        dist[char] = 1

# Displaying character frequencies
print("Character frequencies:")
for char, freq in dist.items():
    print(f"'{char}': {freq}")
