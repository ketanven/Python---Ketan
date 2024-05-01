def prime():
    num = int(input("ENTER A NUMBER = "))
    c = 0
    
    for i in range(1,num+1):
      
        if (num%i==0):
         c+=1
        
    if c ==2:
      return num,"is a prime"
    else:
            return num,"is not a prime"
    

print(prime())
    