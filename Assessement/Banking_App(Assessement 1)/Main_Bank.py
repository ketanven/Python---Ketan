from Menu import banker_menu, customer_menu
from Banker import customers

#____________Define the main function that controls the flow of the banking application__________________
def mainbank():
    while True:
        try:
            # Display the role selection menu
            print("WELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
            print("\nSelect your role")
            print("1) Banker")
            print("2) Customer")
            print("3) Exit")
            
            # Prompt the user to choose their role
            role = int(input("Choose your role: "))

            # If the user is a banker, show the banker menu
            if role == 1:
                banker_menu()
            
            # If the user is a customer, ask for their account number
            elif role == 2:
                account_no = int(input("Enter your account number: "))
                
                # Check if the account number exists in the customers dictionary
                if account_no in customers:
                    customer_menu(account_no)
                else:
                    print("Account not found.")
            
            # If the user wants to exit, break the loop and exit the program
            elif role == 3:
                print("Exiting... Thank You For Using My Software")
                break
            
            # If the user enters an invalid choice, inform them
            else:
                print("Invalid choice.")
        
        # Handle exceptions that may occur, such as invalid input
        except Exception as e:
            print("An unexpected error occurred. Returning to the previous menu.(--ENTER ONLY NUMBERS--)", e)

# Call the main function to start the program
mainbank()
