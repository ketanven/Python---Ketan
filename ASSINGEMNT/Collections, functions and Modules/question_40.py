# Write a Python function to check whether a number is in a given range


def check(number, start, end):
    # Check if the number is in the range
    if start <= number <= end:
        return True
    else:
        return False

# Ask the user for input
num = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end= int(input("Enter the end of the range: "))

# Check if the number is in the range and print the result
if check(num, start, end):
    print(f"{num} is in the range from {start} to {end}")
else:
    print(f"{num} is not in the range from {start} to {end}")
