dist = {}
print("""             WLECOME TO THE PYTHON MANAGEMENT SYSTEM
                           Select your Role
                              1) Banker 
                              2) Customer
                    
                              3) Exit
""")

def Banker():
    
    choice = int(input("Chosse your role : "))
    
    if choice == 1:
        print("""
              Welcome to Banker's App
                                    Operations Menu
                                    1) Add Customer
                                    2) View Customer
                                    3) Search Customer
                                    4) View All Customer
                                    5) Total Amounts in Bank
              
              """)
        operation = int(input(print("Enter operation which you want to perform : ")))
        if operation ==1:
            AccountNumber = int(input("Enter account no : "))
            CustomerName = input("Enter customer name :")
            OpeningBalance = int(input("Enter opening balance : "))
    
            dist["Anumber"] = AccountNumber
            dist["Cname"] = CustomerName
            dist["Obalance"] = OpeningBalance
            
        elif operation == 2:
