num1 = int(input("ENTER A NUM1 : "))
num2 = int(input("ENTER A NUM2 :"))



print("SWAPPING USING TEMP")
print()

print("***BEFOR SWAPPING***")

print("VALUE OF NUM1 = ",num1)
print("VALUE OF NUM2 = ",num2)

temp = num1
num1 = num2
num2 = temp

print()


print("***AFTER SWAPPING***")
print("VALUE OF A = ",num1)
print("VALUE OF B = ",num2)

print()

print("SWAPPING WITHOUT TEMP",num1)
print()


print("***BEFOR SWAPPING***")

print("VALUE OF NUM1 = ",num1)
print("VALUE OF NUM2 = ",num2)

num1,num2 = num2,num1

print()
print("***AFTER SWAPPING***")

print("VALUE OF NUM1 = ",num1)

print("VALUE OF NUM2 = ",num2)