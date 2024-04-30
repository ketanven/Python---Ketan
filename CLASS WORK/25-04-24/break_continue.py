n = int(input("ENTER A NUMBER = "))


for i in range(1,n+1):
    if i == 5:
        break
    print(i)
    
n = int(input("ENTER A NUMBER = ")) 

for i in range(1,n+1):
    if i == 6:
        continue
    print(i)