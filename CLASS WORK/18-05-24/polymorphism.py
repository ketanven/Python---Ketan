class pqr:
    def fun1(self):
        print("THIS IS CLASS PQR")


class abc:
    def fun1(self):
        super().fun1()

        print("THIS IS CLASS ABC")
        
class xyz(abc,pqr):
    
    def fun1(self):
        super().fun1()
        print("THIS IS CLASS XYZ")

obj = xyz()
obj.fun1()