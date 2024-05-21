class user:
    def get(self,__a,__b):
        self.__g = __a
        self.__h = __b

    def set(self):
        print("VALUE OF A = ",self.__g)
        print("VALUE OF B = ",self.__h)
    
    
obj = user()
obj.get(10,20)
obj.set()
     