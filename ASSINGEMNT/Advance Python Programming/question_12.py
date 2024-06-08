#Write python program that user to enter only odd numbers,
# else will
#raise an exception.

def number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 != 0:
                return num
            else:
                raise ValueError("Please enter an odd number.")
        except ValueError as e:
            print(e)

# Example usage:
odd_number = number()
print("You entered:", odd_number)
