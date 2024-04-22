num1 = int(input("ENTER NUMBER 1 : "))
num2 = int(input("ENTER NUMBER 2 : "))
num3 = int(input("ENTER NUMBER 3 : "))


if num1 > num2 and num1 > num3:
    print("NUM1 IS GREATEST")

elif num2 > num1 and num2 > num3:
    print("NUM2 IS GREATEST")

else:
    print("NUM3 IS GREATEST")