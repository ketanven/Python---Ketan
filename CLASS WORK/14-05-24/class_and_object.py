class ketan:
    def mul(self):
        print()
        num1 = int(input("ENTER NUMBER ONE  = "))
        print()
        num2 = int(input("ENTYER NUMBER TWO = "))
        print()
        mul = num1*num2
        print()
        print("MULTIPLICATION OF THE NUIMBER IS  = ",mul)
        print()
    
    def fact(self):
        fact = 1
        num = int(input("ENTER A NUMBER FOR FACTORIAL = "))
        print()
        for i in range(1,num+1):
            fact*=i
        
        print("FACTORIAL OF THE NUMBER IS  = ",fact)
        print()
        
    def add(self):
        print()
        num1 = int(input("ENTER NUMBER ONE = "))
        print()
        num2 = int(input("ENTER NUMBER TWO = "))
        print()
        add = num1+num2
        
        print("ADDITION OF THE NUMBER IS  = ",add)
        print()
        
obj = ketan()
obj.add()
obj.fact()
obj.mul()