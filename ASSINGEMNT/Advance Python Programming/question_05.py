#Write a Python program to read a file line 
# by line and store it into a list

def read():
    lines = []
    file =  open("python.txt", 'r')
    for i in file:
        lines.append(i.strip())
    return lines


lines = read()

# Print the lines to verify
for i in lines:
    print(i)
    
print(lines)
