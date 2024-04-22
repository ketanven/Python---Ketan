i=1
evencount = 0
oddcount = 0
evensum = 0
oddsum = 0

while(i<=5):
    n = int(input("enter number :"))
    if (n%2 == 0):
        print(n,"is even")
        evencount+=1
        evensum += n

    else:
        print(n,"is odd")
        oddcount+=1
        oddsum+=n
    i+=1



print("Total even numbers are :",evencount)
print("Total odd numbers are :",oddcount)
print("sum of even numbers are :",evensum)
print("sum of  odd numbers are :",oddsum)