
num = int(input("ENTER A NUMBER FOR FACTORIAL : "))

if num < 0:
    print("**ENYTERD NUMBER IS NEGATIVE SO FACTORIAL IS NOT POSSIBLE")
else:
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    
    print("**FACTORIAL OF THE GIVEN NUMBER IS : ",fact)