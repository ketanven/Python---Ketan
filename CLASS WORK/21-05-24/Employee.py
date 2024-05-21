from abc import ABC,abstractmethod

class Salary(ABC):
    def tsalary(self):
        pass
    
class Ketan(Salary):
    def tsalary(self):
        print("Ketan got 20k salary")
    
class Uday(Salary):
    def tsalary(self):
        print("Uday got 22k salary")
    
class Jay(Salary):
    def tsalary(self):
        print("Jay got 25k salary")
        
class Ketki(Salary):
    def tsalary(self):
        print("Ketki got 30k salary")
    
obj = Ketan()
obj.tsalary()

obj1 = Uday()
obj1.tsalary()

obj2 = Jay()
obj2.tsalary()

obj3 = Ketki()
obj3.tsalary()