# Write a Python function to get the largest number, smallest num and sum
# of all from a list.


def find():
    # Define a list of numbers
    list = [10, 22, 33, 11, 33, 44, 66, 77, 11, 88, 99]
    
    # Sort the list in ascending order
    list.sort()
    
    # Print the smallest number in the sorted list (which is the first element)
    print("SMALLEST NUMBER IN THE LIST IS = ", list[0])
   
    # Print the largest number in the sorted list (which is the last element)
    print("LARGEST NUMBER IN THE LIST IS = ", list[-1])
    
    # Calculate and print the sum of all numbers in the list
    print("SUM OF THE LIST IS = ", sum(list))   

# Call the find function to execute the above steps
find()
