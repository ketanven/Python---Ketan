# Write a Python program to find whether a given number is even or odd,
# print out an appropriate message to the user.

# Take input from the user
num = int(input("**ENTER A NUMBER TO CHECK EVEN OR ODD : "))

print()

# Check if the number is zero
if num == 0:
    print("**ENTERED NUMBER IS ZERO**")
    print()
    
# Check if the number is even
elif num % 2 == 0:
    print("**ENTERED NUMBER IS EVEN**")
    print()

# If not zero and not even, then it must be odd
else:
    print("**ENTERED NUMBER IS ODD**")
    print()
