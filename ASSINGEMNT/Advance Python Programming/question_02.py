#Write a Python program to append text to a file 
# and display the text

# Open the file in append mode
file = open("python.txt", "a")
    # Append text to the file
file.write("\nThis is some appended text.")

# Open the file again in read mode to display the contents
file = open("python.txt", "r")
    # Read the entire contents of the file
contents = file.read()

# Print the contents
print(contents)
