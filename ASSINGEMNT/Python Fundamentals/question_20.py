# Write a Python function that takes a list of words and returns the length
# of the longest one


def long(words):
    return max(len(word) for word in words)

# Ask the user to input a list of words
word_list = input("Enter a list of words separated by spaces: ").split()

# Output the length of the longest word
print("Length of the longest word:", long(word_list))
