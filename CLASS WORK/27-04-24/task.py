while True:
    menu = """

            *******WELCOME!!*******
            
            1.ADDITION(+)
            2.SUBTRACTION(-)
            3.MULTIPLICATION(*)
            4.DIVISION(/)
            5.EXIT
            
"""
    print(menu)
    print()
    choice = int(input("PLEASE ENTER YOUR CHOICE (1-4) = "))

    if choice == 1:
        num1 = int(input("ENTER A NUMBER 1 = "))
      
        num2 = int(input("ENTER A NUMBER 2 = "))
        
    
        print("ADDITION IS = ",num1+num2)
        print()
    
    elif choice ==2:
        num1 = int(input("ENTER A NUMBER 1 = "))
        num2 = int(input("ENTER A NUMBER 2 = "))
    
        print("SUBTRATCION IS = ",num1-num2)
        print()
    
    elif choice ==3:
        num1 = int(input("ENTER A NUMBER 1 = "))
        num2 = int(input("ENTER A NUMBER 2 = "))
    
        print("MULTIPLICATION IS = ",num1*num2)
        print()
    
    elif choice == 4:
        num1 = int(input("ENTER A NUMBER 1 = "))
        num2 = int(input("ENTER A NUMBER 2 = "))
    
        print("DIVISION IS = ",num1/num2)
        print()
    
    elif choice == 5:
        print("**THANKS FOR USING THE SOFTWARE**")
        print()
        break;
        
    else:
        print("INVALID CHOICE ):")
        print()
        break;
