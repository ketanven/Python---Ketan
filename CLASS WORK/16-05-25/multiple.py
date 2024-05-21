class A:
    def father(self):
        print("----THIS IS PARENT CLASS----")

class B:
    def mother(self):
        print("----THIS IS SECOND PARENT----")
    
class C(A,B):
    def child(self):
        print("----THIS IS CHLID CLASS----")
    
    
obj = C()
obj.father()
obj.mother()
obj.child()