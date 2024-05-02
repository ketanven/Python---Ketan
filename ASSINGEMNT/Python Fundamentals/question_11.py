# Write a python program to sum of the first n positive integers.

# Take input from the user for a positive number
print()
num = int(input("**PLEASE ENTER A POSITIVE NUMBER = "))
print()

# Initialize total sum variable
total = 0

# Loop through positive integers up to the input number and calculate their sum
for i in range(1, num + 1):
    total += i

# Print the sum of the first 'num' positive integers
print(f"**THE SUM OF THE FIRST {num} POSITIVE INTEGERS IS: {total}")
print()
