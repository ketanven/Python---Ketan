# Write a Python program to count the occurrences of each word in a
# given sentence
# Input sentence
sentence = input("Enter a sentence: ")

# Splitting the sentence into words
words = sentence.split()

# Dictionary to store word frequencies
word_freq = {}

# Counting word occurrences
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Displaying word frequencies
print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"'{word}': {freq}")
