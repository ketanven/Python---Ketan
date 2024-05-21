class A:
    def father(self):
        print("----THIS IS PARENT CLASS----")

class B(A):
    def mother(self):
        print("----THIS IS SECOND PARENT----")
    
class C(A):
    def child(self):
        print("----THIS IS CHLID CLASS----")
    
    
obj1 = B()
obj1.father()
obj1.mother() 

obj = C()
obj.child()
