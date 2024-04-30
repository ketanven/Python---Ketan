
def factorial(num):
    if num <= 0:
        print("**ENTERED NUMBER IS NEGATIVE SO FACTORIAL IS NOT POSSIBLE")
    else:
        fact = 1
    for i in range(1,num+1):
        fact = fact*i
    
    print("**FACTORIAL OF THE GIVEN NUMBER IS : ",fact)
    
    
num = int(input("ENTER A NUMBER FOR FACTORIAL : "))
factorial(num)
print()

# ================================================================

def add(a,b):
    print("ADDITION IS = ",a+b)

num1 = int(input("ENTER NUM1 = "))
num2 = int(input("ENTER NUM2 = "))

add(num1,num2)
print()

# ================================================================




def sub(a,b):
    print("ADDITION IS = ",a-b)

num1 = int(input("ENTER NUM1 = "))
num2 = int(input("ENTER NUM2 = "))

sub(num1,num2)
print()

# ================================================================

def mul(a,b):
    print("ADDITION IS = ",a*b)

num1 = int(input("ENTER NUM1 = "))
num2 = int(input("ENTER NUM2 = "))

mul(num1,num2)
print()

# ================================================================

def div(a,b):
    print("ADDITION IS = ",a/b)

num1 = int(input("ENTER NUM1 = "))
num2 = int(input("ENTER NUM2 = "))

div(num1,num2)
print()