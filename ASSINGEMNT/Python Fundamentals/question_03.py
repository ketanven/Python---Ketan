# Write a Python program to get the Fibonacci series of given range.


print()
num = int(input("** Enter the maximum value for Fibonacci series: "))
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



n  = int(input("** Enter the maximum value for Fibonacci series: "))
n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(3,n+1):
    n3 = n1+n2
    print(n3)
    n1=n2
    n2=n3
    print()  
