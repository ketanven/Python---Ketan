import datetime

# Dictionary to store customer details with account number as key
customers = {}



# ______________________Function to add a new customer_______________________________________________________________

def add_customer(account_no, name, balance):
    try:
        # Check if account number already exists
        if account_no in customers:
            print("Account number already exists. Please choose a different account number.")
            return
        
        # Add the new customer to the dictionary with the current date and time as the opening date
        customers[account_no] = {'name': name, 'balance': balance, 'Opening Date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
   
    except ValueError as e:
        # Handle any value errors that may occur and print an error message
        print("An unexpected error occurred in add_customer. Returning to the previous menu.", e)

#________________________________________________________________________________________



# __________________________Function to view details of a specific customer_________________

def view_customer(account_no):
    try:
        # Check if the account number exists in the dictionary
        if account_no in customers:
            customer_details = customers[account_no]
            # Print the details of the customer
            print(f"{account_no}: {customer_details}")
        else:
            # Print message if customer is not found
            print("Customer not found.")
    except Exception as e:
        # Handle any exceptions that may occur and print an error message
        print("An unexpected error occurred in view_customer. Returning to the previous menu.", e)

#_____________________________________________________________________________________________________




# ______________________________Function to search for a customer by name_________________________________


def search_customer(name):
    try:
        found = False
        # Iterate through the dictionary to find the customer by name
        for acc_no, info in customers.items():
            if info['name'] == name:
                print(f"Account No: {acc_no}, Name: {name}, Balance: {info['balance']}")
                found = True
        if not found:
            # Print message if customer is not found
            print("Customer not found.")
    except Exception as e:
        # Handle any exceptions that may occur and print an error message
        print("An unexpected error occurred in search_customer. Returning to the previous menu.", e)

#______________________________________________________________________________________________


#_________________________Function to calculate and print the total amount of all customer balances____________

def total_amounts():
    try:
        # Calculate the sum of all customer balances
        total = sum(info['balance'] for info in customers.values())
        print(f"Total Amounts in Bank: {total}")
    except Exception as e:
        # Handle any exceptions that may occur and print an error message
        print("An unexpected error occurred in total_amounts. Returning to the previous menu.", e)

#____________________________________________________________________________________________________



#________________________Function to view details of all customers__________________________________

def view_all_customers():
    try:
        if customers:
            print("All Customers:")
            # Iterate through the dictionary and print details of each customer
            for account_no, info in customers.items():
                print(f"{account_no}: {{'name': '{info['name']}', 'balance': {info['balance']}, 'Opening Date': '{info['Opening Date']}'}}")
        else:
            # Print message if no customers are found
            print("No customers found.")
    except Exception as e:
        # Handle any exceptions that may occur and print an error message
        print("An unexpected error occurred in view_all_customers. Returning to the previous menu.", e)

#________________________________________________________________________________________________________