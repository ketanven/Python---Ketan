from Banker import customers
from utils import log_transaction
#___________________Function to withdraw an amount from a customer's account_________________

def withdraw(account_no, amount):
    try:
        # Get the current balance of the customer
        balance = customers[account_no]['balance']
        
        # Check if the balance is sufficient for the withdrawal
        if amount > balance:
            print("Insufficient balance.")
        else:
            # Deduct the amount from the balance
            balance -= amount
            
            # Update the balance in the customers dictionary
            customers[account_no]['balance'] = balance
            print("Withdrawal successful.")
            print(f"Available Balance: {balance}")
            
        log_transaction(account_no, customers[account_no]['name'], balance, "Withdrawal", amount)

            
    except Exception as e:
        # Handle any exceptions that may occur and print an error message
        print("An unexpected error occurred in withdraw. Returning to the previous menu.", e)

#___________________________________________________________________________________________________


#________________Function to deposit an amount into a customer's account_______________________

def deposit(account_no, amount):
    try:
        # Get the current balance of the customer
        balance = customers[account_no]['balance']
        
        # Add the amount to the balance
        balance += amount
        
        # Update the balance in the customers dictionary
        customers[account_no]['balance'] = balance
        print("Deposit successful.")
        print(f"Available Balance: {balance}")
        log_transaction(account_no, customers[account_no]['name'], balance, "Deposit", amount)

        
    except Exception as e:
        # Handle any exceptions that may occur and print an error message
        print("An unexpected error occurred in deposit. Returning to the previous menu.", e)

#______________________________________________________________________________________________