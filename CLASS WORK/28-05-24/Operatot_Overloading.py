#Magic Methods   

class User:
    def __init__(self,a,b): #init Called directly when obj is crearted
        print("Init Called**")
        self.x = a
        self.y = b
        
    def __str__(self):#str called directly when obj got printed
        print("Str Called**")
        return "{0}","{1}".format(self.x,self.y)
    
    def __add__(self,obj):#addition of two obj taking one more para in the function
        print("Add called")
        x = self.x+obj.x
        y = self.y+obj.y
        
        return(x,y)
    
    
obj = User(20,30)
print(obj)

obj1 = User(30,40)
print(obj1)

print("Addition is ",obj+obj1)