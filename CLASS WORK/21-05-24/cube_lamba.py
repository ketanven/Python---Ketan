# a = lambda x,y,z :x*y*z

# print("Cube  = ",a(10,10,10))


A =[10,20,44,67,23]

result = filter(lambda x:x%2 == 0,A)

result2 = map(lambda x:x*x,A)


for i in result:
    print(i,end=" ")
    
for j in result2:
    print()
        
    print(j,end=" ")

