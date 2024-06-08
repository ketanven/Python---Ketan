#Write a Python program to read a file line by line 
# store it into a variable.

def read():
    content = ""
    file =  open("python.txt", 'r')
    for i in file:
        content += i
    return content

content = read()

# Print the content to verify
print(content)
