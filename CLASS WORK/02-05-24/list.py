list = [1,"ketan","pillai",23.333,1,2,1,1,1,90909.67564]

list.append("Pillai")
print(list)


list.copy()
print(list)

print(list.count(1))

list.index(2)
print(list)


list.insert(1,"Uday")
print(list)


list.pop(5)
print(list)


list.reverse()
print(list)


list.extend(["Rajput",22,44,77,90.767])
print(list)

a = frozenset(list)
print("frozenset is",a)

print(type(a))





