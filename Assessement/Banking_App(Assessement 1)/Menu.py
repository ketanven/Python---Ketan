from Banker import add_customer, view_customer, search_customer, total_amounts, view_all_customers
from Customer import withdraw, deposit
from utils import log_transaction
from Banker import customers

def banker_menu():
    """
    Function to display and handle the banker's menu operations.
    """
    while True:
        try:
            # Display the banker's menu
            print("\nWelcome to Banker's App")
            print("Operations Menu")
            print("1) Add Customer")
            print("2) View Customer")
            print("3) Search Customer")
            print("4) View All Customers")
            print("5) Total Amounts in Bank")
            choice = int(input("Enter operation which you want to perform: "))

            if choice == 1:
                try:
                    # Add a new customer
                    account_no = int(input("Enter account no: "))
                    name = input("Enter customer name: ")
                    balance = int(input("Enter opening balance: "))
                    add_customer(account_no, name, balance)
                    log_transaction(account_no, name, balance, "Add Customer", balance)
                except ValueError as e:
                    # Handle invalid input
                    print("Invalid input. Please enter the correct details.", e)
            elif choice == 2:
                try:
                    # View an existing customer
                    account_no = int(input("Enter account no: "))
                    view_customer(account_no)
                except ValueError as e:
                    # Handle invalid account number input
                    print("Invalid input. Please enter a valid account number.", e)
                except Exception as e:
                    # Handle unexpected errors
                    print("An unexpected error occurred. Returning to the previous menu.", e)
            elif choice == 3:
                try:
                    # Search for a customer by name
                    name = input("Enter customer name: ")
                    search_customer(name)
                except Exception as e:
                    # Handle unexpected errors
                    print("An unexpected error occurred. Returning to the previous menu.", e)
            elif choice == 4:
                try:
                    # View all customers
                    view_all_customers()
                except Exception as e:
                    # Handle unexpected errors
                    print("An unexpected error occurred. Returning to the previous menu.", e)
            elif choice == 5:
                try:
                    # View total amounts in the bank
                    total_amounts()
                except Exception as e:
                    # Handle unexpected errors
                    print("An unexpected error occurred. Returning to the previous menu.", e)
            else:
                # Handle invalid menu choice
                print("Invalid choice.")

            # Ask if the banker wants to perform more operations
            more = input("Do you want more operations? (y/n): ")
            if more.lower() != 'y':
                break
        except Exception as e:
            # Handle unexpected errors in the main banker menu loop
            print("An unexpected error occurred in banker_menu. Returning to the previous menu.", e)

def customer_menu(account_no):
    """
    Function to display and handle the customer's menu operations.
    """
    while True:
        try:
            # Display the customer's menu
            print("\nWelcome to Customer's App")
            print("Operations Menu")
            print("1) Withdraw Amount")
            print("2) Deposit Amount")
            print("3) View Balance")
            choice = int(input("Enter operation which you want to perform: "))

            if choice == 1:
                try:
                    # Withdraw amount from the customer's account
                    amount = float(input("Enter amount to withdraw: "))
                    withdraw(account_no, amount)
                except ValueError as e:
                    # Handle invalid amount input
                    print("Invalid input. Please enter the correct amount.", e)
                except Exception as e:
                    # Handle unexpected errors during withdrawal
                    print("An unexpected error occurred in customer_menu during withdrawal. Returning to the previous menu.", e)
            elif choice == 2:
                try:
                    # Deposit amount into the customer's account
                    amount = float(input("Enter amount to deposit: "))
                    deposit(account_no, amount)
                except ValueError as e:
                    # Handle invalid amount input
                    print("Invalid input. Please enter the correct amount.", e)
                except Exception as e:
                    # Handle unexpected errors during deposit
                    print("An unexpected error occurred in customer_menu during deposit. Returning to the previous menu.", e)
            elif choice == 3:
                try:
                    # View the balance of the customer's account
                    balance = customers[account_no]['balance']
                    print(f"Available Balance: {balance}")
                except KeyError:
                    # Handle case where the account is not found
                    print("Account not found.")
                except Exception as e:
                    # Handle unexpected errors during balance check
                    print("An unexpected error occurred in customer_menu during balance check. Returning to the previous menu.", e)
            else:
                # Handle invalid menu choice
                print("Invalid choice.")

            # Ask if the customer wants to perform more operations
            more = input("Do you want to perform more operations? (y/n): ")
            if more.lower() != 'y':
                break
        except Exception as e:
            # Handle unexpected errors in the main customer menu loop
            print("An unexpected error occurred in customer_menu. Returning to the previous menu.", e)
