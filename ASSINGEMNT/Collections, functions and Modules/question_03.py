# Write a Python program to remove duplicates from a list.

list = [22,33,44,22,55,11,55,22,22,33,44,"ketan","ketan"]


result1 = set(list)

result2 = frozenset(list)

print()
print("DUPLICATES REMOVED NEW LIST = ",result1)

print()

print("DUPLICATES REMOVED NEW LIST = ",result2)
print()