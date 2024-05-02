list = [1,2,3,4,5,1,2,3]
list2 = []
list3 = []

for i in list:
    if i not in list2:
        list2.append(i)
    else:
        list3.append(i)
        

print(list)
print(list2)
print(list3) 