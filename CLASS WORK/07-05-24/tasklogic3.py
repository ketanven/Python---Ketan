# l = [1,2,3]

# l1 = [4,5,6]


# d = {}


# for i in l:
#     for j in l1:
#      d[i] =j
#      l1.remove(j)
#      break 
    
# print(d)
    
    


l = [1, 2, 3]
l1 = [4, 5, 6]

d = {}

# Iterate over indices of l and l1
for i in range(len(l)):
    # Use index to access elements from l and l1
    key = l[i]
    value = l1[i]
    d[key] = value

print(d)
print(l)
print(l1)



