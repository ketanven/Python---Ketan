
d ={}
while True:
    menu = """
    Press 1 : Sign Up
    Press 2 : Login
    Press 3 : Exit
    """
    
    print(menu)
    
    choice = int(input("ENTER YOUR CHOICE = "))
    
    if choice == 1:
        print("SIGN UP HERE !!!!")
        
        Name = input("ENTER YOUR NAME = ")
        Email = input("ENTER YOUR EMAIL = ")
        Password = input("ENTER YOUR PASSWORD = ")
        Cpassword = input("ENTER CONFIRM PASSWORD = ")
      
        
        file = open("C:\\Users\\LENOVO\\Desktop\\Python---Ketan\\CLASS WORK\\11-05-24\\login.txt","w")
        
        d["login"] = {'Name':Name,
            'Email':Email,
            'Password':Password
            }
        d1 = str(d)
        print(type(d1))
        file.write(d1)
       
        
        file.close()
        
        if Password == Cpassword:
            print("****SIGN UP SUCCESSFULLY DONE***")
        else:
            print("!!!PASSWORD DOES NOT MATCHED!!!")
        
    elif choice == 2:
        print("LOGIN HERE!!!")
        
        Email = input("ENTER YOUR EMAIL = ")
        
        Password = input("ENTER YOUR PASSWORD = ")
        
        if d["Email"] == Email and d["Password"] == Password:
            print("***LOGIN SUCCESSFULLY DONE***")
        else:
            print("!!INVALID CREDETIAILS")
    
    elif choice == 3:
        print("---THANKS FOR USING ! GREAT DAY---")
    
    else:
        print("**INVALID CHOICE***") 
    
    break
        
        