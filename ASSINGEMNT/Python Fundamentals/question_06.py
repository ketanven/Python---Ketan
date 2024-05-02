# Write python program that swap two number with temp variable and
# without temp variable.

# Take input from the user
num1 = int(input("ENTER A NUM1 : "))
num2 = int(input("ENTER A NUM2 : "))

# Swapping using a temporary variable
print("SWAPPING USING TEMP")
print()

print("***BEFORE SWAPPING***")

print("VALUE OF NUM1 = ", num1)
print("VALUE OF NUM2 = ", num2)

# Swapping using a temporary variable
temp = num1
num1 = num2
num2 = temp

print()

print("***AFTER SWAPPING***")
print("VALUE OF NUM1 = ", num1)
print("VALUE OF NUM2 = ", num2)

print()

# Swapping without using a temporary variable
print("SWAPPING WITHOUT TEMP")
print()

print("***BEFORE SWAPPING***")

print("VALUE OF NUM1 = ", num1)
print("VALUE OF NUM2 = ", num2)

# Swapping without using a temporary variable
num1, num2 = num2, num1

print()
print("***AFTER SWAPPING***")

print("VALUE OF NUM1 = ", num1)
print("VALUE OF NUM2 = ", num2)
