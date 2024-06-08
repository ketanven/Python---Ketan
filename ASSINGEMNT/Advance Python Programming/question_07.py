#Write a python program to find the longest words.

def find():
    longest = ''
    file = open("python.txt", 'r')
    for i in file:
            for word in i.split():
                if len(word) > len(longest):
                    longest = word
    return longest

longest = find()

# Print the longest word to verify
print("Longest word:", longest)
