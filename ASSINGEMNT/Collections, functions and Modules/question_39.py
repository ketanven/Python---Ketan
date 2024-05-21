# # Write a Python function to calculate the factorial of a number (a
# nonnegative integer)


def factorial():
    # Ask the user for input
    num = int(input("Enter a Number for Factorial: "))
    
    # Check if the number is zero
    if num == 0:
        return print("Enter number is zero")  # If the number is zero, print a message and exit the function
    
    else:
        # Initialize the factorial variable to 1
        fact = 1
        
        # Calculate the factorial using a loop
        for i in range(1, num + 1):
            fact = fact * i  # Multiply the current value of fact by the current value of i
        
        # Print the factorial
        print("Factorial of", num, "is", fact)

# Call the function
factorial()
