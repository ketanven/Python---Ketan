
num = int(input("Enter the maximum value for Fibonacci series: "))

# Initialize the first two numbers in the Fibonacci sequence
a, b = 0, 1

# Print the Fibonacci sequence up to the maximum value
while a <= num:
    print(a, end=" ")  # Print the current Fibonacci number
    a, b = b, a + b    # Update the Fibonacci sequence (next Fibonacci number)

    # Break the loop if the next Fibonacci number exceeds the maximum value
    if a > num:
        break

print()  # Move to the next line after printing the series
