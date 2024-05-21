#Write a Python program to returns sum of all divisors of a number

def sum_of_divisors(number):
    # Initialize sum
    divisors_sum = 0
    # Find all divisors
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum

# Ask the user for input
num = int(input("Enter a number: "))

# Calculate and print the sum of divisors
print("Sum of divisors of", num, "is", sum_of_divisors(num))
