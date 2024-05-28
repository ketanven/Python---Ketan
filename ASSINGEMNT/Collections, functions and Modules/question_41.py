#Write a Python function to check whether a number is perfect or not    

def perfect(number):
    # Calculate the sum of factors
    sum_factors = sum(i for i in range(1, number) if number % i == 0)
    
    # Check if the sum of factors equals the number itself
    return sum_factors == number

# Ask the user for input
num = int(input("Enter a number: "))

# Check if the number is perfect and print the result
if perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

