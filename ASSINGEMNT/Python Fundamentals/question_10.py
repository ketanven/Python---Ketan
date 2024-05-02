# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

# Take input from the user for two integers
num1 = int(input("**ENTER FIRST INTEGER = "))
print()
num2 = int(input("**ENTER SECOND INTEGER = "))
print()

# Check if the two numbers are equal
if num1 == num2:
    print(True)
    print()

# Check if the sum of the two numbers is 5
elif num1 + num2 == 5:
    print(True)
    print()

# Check if the absolute difference between the two numbers is 5
elif abs(num1 - num2) == 5:
    print(True)
    print()

# If none of the above conditions are met, print False
else:
    print(False)
    print()
