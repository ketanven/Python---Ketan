# Write a Python function that takes two lists and returns true if they have at least one common member.

def check(list1,list2):
    set1 = set(list1)
    
    
    for element in list2:
        if element in set1:
            print("YES!! SOME OF ELEMENTS ARE SAME IN BOHT THE LIST")
            return True
    
    return False
    

list1 = [22,33,44,55,"ketan","pillai",22,66]

list2 = [22,33,77,67,34,23,45,67,78,87,76,65]

# list2 = [77,88,99,999,89,89,89] //output = false


print(check(list1,list2))






