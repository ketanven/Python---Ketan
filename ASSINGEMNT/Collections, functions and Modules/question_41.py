#Write a Python function to check whether a number is perfect or not    


def is_perfect(number):
    # Initialize sum of factors
    sum_factors = 0
    
    # Find all factors of the number
    for i in range(1, number):
        if number % i == 0:
            sum_factors += i
    
    # Check if the sum of factors equals the number itself
    return sum_factors == number

# Ask the user for input
num = int(input("Enter a number: "))

# Check if the number is perfect and print the result
if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
