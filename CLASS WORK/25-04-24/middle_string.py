s = input("**ENTER A STRING = ")

l1 = int (len(s)/2)


if len(s) %2==0:
    print(s)

else:
    print(s[l1]+s[l1+1])

