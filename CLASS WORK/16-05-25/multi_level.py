class G:
    def home(self):
        print("THIS IS MULTI LEVEL INHERTINACE****")


class A(G):
    def mul(self):
        num = int(input("ENTER NUMBER ONE  = "))
        num2 = int(input("ENTER NUMBER TWO = "))
        print("MULTIPLICATION OF THE NUMBER ARE = ",num*num2)
        
class B(A):
    def result(self):
        print("MULTIPLICATION OF THE NUMBER")
        
obj = B()
obj.home()
obj.mul()
obj.result()