class A:
    def father(self):
        print("----THIS IS PARENT CLASS----")

class B(A):
    def mother(self):
        print("----THIS IS SECOND PARENT----")
    
class C():
    def child(self):
        print("----THIS IS CHLID CLASS----")

class D(B,C):
    def subchild(self):
        print("----THIS IS SUB CHILD OF HYBRID----")
    
    
obj = D()
obj.father()
obj.mother()
obj.subchild()
obj.child()


