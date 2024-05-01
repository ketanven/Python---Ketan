def prime(a):
    c = 0
    
    for i in range(1,a+1):
      
        if (a%i==0):
         c+=1
        
    if c ==2:
      return a,"is a prime"
    else:
        return a,"is not a prime"
    

print(prime(7))
    