from abc import ABC,abstractmethod

class RBI(ABC):
    def roi(self):
        pass
    
class Kotak(RBI):
    def roi(self):
        print("kotak got 9.0%")
    
class SBI(RBI):
    def roi(self):
        print("sbi got 8.9%")
    
class HDFC(RBI):
    def roi(self):
        print("HDFC got 8.0%")
    
obj = Kotak()
obj.roi()

obj1 = SBI()
obj1.roi()

obj2 = HDFC()
obj2.roi()