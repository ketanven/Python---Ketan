#Write a Python program to read last n lines of a file.

def read(n):
    file = open("python.txt", 'r')
    lines = file.readlines()
    
    # Get the last n lines
    last = lines[-n:]
    
    for line in last:
        print(line.strip())

n = 5  
read(n)
