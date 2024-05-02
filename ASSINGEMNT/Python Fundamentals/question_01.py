# Write a Python program to check if a number is positive, negative or
# zero.

# Take input from the user
num = int(input("ENTER ANY NUMBER : "))

# Check if the number is zero
if num == 0:
    print("**ENTERED NUMBER IS ZERO**")

# Check if the number is positive
elif num > 0:
    print("**ENTERED NUMBER IS POSITIVE**")

# If the number is not zero or positive, it must be negative
else:
    print("**ENTERED NUMBER IS NEGATIVE**")
