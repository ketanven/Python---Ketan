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

# Iterate over elements of l and l1 simultaneously
for key, value in zip(l, l1):
    d[key] = value

print(d)
print(l)
print(l1)




