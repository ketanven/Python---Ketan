# Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.

# Take input from the user for three numbers
num1 = int(input("ENTER NUMBER 1 = "))
print()
num2 = int(input("ENTER NUMBER 2 = "))
print()
num3 = int(input("ENTER NUMBER 3 = "))
print()

# Check if any two numbers are the same
if num1 == num2 or num2 == num3 or num1 == num3:
    print("**ANY TWO OF THE ENTERED NUMBERS ARE THE SAME, SO SUM CAN'T BE DONE**")
    print("SUM = 0")
    print()

# If all three numbers are different, calculate their sum
else:
    print("SUM OF ALL THREE GIVEN NUMBERS IS = ", num1 + num2 + num3)
    print()
