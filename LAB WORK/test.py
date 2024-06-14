# # list1 =[]

# # for i in list:
# #     if i not in list1:
# #         list1.append(i)


# # list1 = []

# # i = [i**2 for i in range(1,31)]

# # list =  ["k","e","t","a","n"]

# # string = ""

# # for i in list:
# #     string += i

# # print(string)



# # import random
# # list = [1,2,3,4,5,11,22,33,44,55,66]

# # result = random.choice(list)

# # print(result)


# # dict1 = {1:"ketan",2:"uday"}

# # dict2 = {3:"raj",4:"jay"}


# # dict3 = dict1.copy()
# # dict3.update(dict2)

# # print(dict3)



# # dict1 ={}


# # for i in range(1,16):
    
# #     dict1[i]=None

# # print(dict1)    

# # fact = 1

# # num = int(input("enter a num"))

# # if num<=1:
# #     print("invalid number")
# # else:
# #         for i in range(2,num):
# #             if num % i ==0:
# #              print("not a prime")
# #              break
# #         else:
# #          print("is a prime")




# # a = 0
# # b = 1

# # num = int(input("enter a number"))



# # for i in range(2,num+1):
# #     a,b = b,a+b
# #     print(b)
    


# evencount = 0
# oddcount = 0
# evensum = 0
# oddsum = 0
# evenlist = []
# oddli = []
# for i in range(1,6):
#     num = int(input("enter a number"))
#     if num == 0:
#      print("invalid number")
     
#     elif num % 2 == 0:
#      print("even number")
#      evencount +=1
#      evensum +=num
#      evenlist.append(num)
#     else:
#      print("odd number")
#      oddcount +=1
#      oddsum +=num
#      oddli.append(num)



# print("evencoutnt :",evencount)
# print("oddcount",oddcount)
# print("odd",evensum)
# print("o",oddsum)
# print(evenlist)
# print(oddli)



num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))

if num1>num2 and num1>num3:
    print("num1 is bigggg")
elif num2>num1 and num2>num3:
    print("num2 is biggggg")
    
else:
    print("num3 is bigggg")

        
        
        