file = open("C:\\Users\\LENOVO\\Desktop\\Python---Ketan\\CLASS WORK\\11-05-24\\test3.txt","w+")

file.write("I M A W+ METHOD********")

print(file.tell())
file.seek(0)

print(file.read())

file.close()