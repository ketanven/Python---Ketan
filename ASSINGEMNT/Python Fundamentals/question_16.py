# Write a Python program to count the occurrences of each word in a
# given sentence

# Input sentence
print()
sentence = input("**Enter a sentence =  ")

# Splitting the sentence into words
words = sentence.split()

# Dictionary to store word frequencies
dist = {}

# Counting word occurrences
for word in words:
    if word in dist:
        dist[word] += 1
    else:
        dist[word] = 1

# Displaying word frequencies
print("----Word occurrences:")
for i, j in dist.items():
    print(f"'{i}': {j}")
