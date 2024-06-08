#Write a Python program to check whether a 
# list contains a sub list


# Main list
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sublist to check
sub_list = [4, 5, 6]

# Check if sublist is found in the main list
if sub_list in [main_list[i:i+len(sub_list)] for i in range(len(main_list) - len(sub_list) + 1)]:
    print("Sublist found in the main list.")
else:
    print("Sublist not found in the main list.")
