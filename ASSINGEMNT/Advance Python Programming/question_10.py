#Write a Python program to write a list to a file.

def write(data):
    file =  open("python.txt", 'w')
    for i in data:
        file.write(str(i) + '\n')


my_list = [1, 2, 3, 4, 5] 
write(my_list)
print("Added Successfully!!")
