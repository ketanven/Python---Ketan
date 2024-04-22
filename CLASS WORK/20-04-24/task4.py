evcount = 0
odcount = 0
evsum=0
odsum=0
for i in range(1,6,1):
    n= int(input("enter a number"))
    
    if n%2==0:
        print("entered number is even")
        evcount+=1
        evsum+=n

    
    else:
        print("entered numbers is odd")
        odcount+=1
        odsum+=n
    

print("total even is ",evcount)
print("total odd is",odcount)
print("sum even is ",evsum)
print("sum odd is ",odsum)


