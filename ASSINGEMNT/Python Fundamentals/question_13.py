# Write a Python program to count the number of characters (character
# frequency) in a string


# Input string
input_string = input("Enter a string: ")

# Dictionary to store character frequencies
char_freq = {}

# Counting characters
for char in input_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Displaying character frequencies
print("Character frequencies:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")
