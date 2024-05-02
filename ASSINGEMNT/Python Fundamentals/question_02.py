# Write a Python program to get the Factorial number of given number.

# Take input from the user
num = int(input("ENTER A NUMBER FOR FACTORIAL : "))

# Check if the number is negative
if num < 0:
    print("**ENTERED NUMBER IS NEGATIVE SO FACTORIAL IS NOT POSSIBLE**")
else:
    # Initialize factorial variable to 1
    fact = 1
    
    # Calculate factorial using a loop
    for i in range(1, num + 1):
        fact = fact * i
    
    # Print the factorial of the given number
    print("**FACTORIAL OF THE GIVEN NUMBER IS : ", fact)
