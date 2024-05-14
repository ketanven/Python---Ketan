import random

l1 = random.randint(1,50)

print("***WELCOME TO THE NUMBER MATCH GAME***")

while True:
    num = int(input("ENTER YOUR CHOICE AS NUMBER (1-50)"))

    if num>l1:
        print("ENTER NUMBER IS HIGHER ! U LOST")
    elif num<l1:
        print("ENTER NUMBER IS LOWER ! U LOST")
    elif num == l1:
        print("ENTER NUMBER IS PERFECTLY MATCHED")
        print("****CONGRULATIONS U WON****")
        break
    else:
       print("INVALID CHOICE ;(")
       break

