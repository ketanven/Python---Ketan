d = {1:"ketan",2:"Uday",3:"Ajay"}


print(d.get(1)) #to get particular value of the key

print(d.items()) #to get the itmes of the dict

print(d.values()) #to get the values of the dict

d.update({4:"Rajesh",5:"Subhash"})# to update the dict same lke extend in list 

print(d)

d.pop(2) #to remove the exact index numbered key and value
print(d)

print(d.popitem())#by default to remove the last key and value

t= (1,2,3)

d1 = d.fromkeys(t,5) #to convert the tuple into dict and add the key and same value

print(d1)



# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("brand", "BMW")

# print(x)



