#Write a Python program to read first n lines of a file.


def read(n):
    file = open("python.txt", 'r')
    for i in range(n):
        line = file.readline()
        if line == '':
            break  # End of file reached
        print(line.strip())


n = 5
read(n)
