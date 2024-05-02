num1 = int(input("ENTER NUMBER 1 = "))
print()
num2 = int(input("ENTER NUMBER 2 = "))
print()
num3 = int(input("ENTER NUMBER 3 = "))
print()


if num1 == num2 or num2 == num3 or num1 == num3:
    print("**ENTERED ANY OF TWO NUMBERS ARE SAME,SO SUM CAN'T BE DONE**")
    print()

else:
    print("SUM OF ALL THREE GIVEN NUMBER IS = ",num1+num2+num3)
    print()