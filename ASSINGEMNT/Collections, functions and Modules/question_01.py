# Write a Python function to get the largest number, smallest num and sum
# of all from a list.


def find():
    list = [10,22,33,11,33,44,66,77,11,88,99]
    
    list.sort()
    
    print("SMALLEST NUMBER IN THE LIST IS = ",list[0])
   
    print("LARGEST NUMBER IN THE LIST IS = ",list[-1])
    
    print("SUM OF THE LIST IS = ",sum(list))   

find()