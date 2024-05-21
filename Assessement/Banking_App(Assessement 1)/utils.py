import datetime

def log_transaction(account_no, name, balance, transaction_type, amount):
    try:
        file =  open("Assessement\\Banking_App(Assessement 1)\\banker_details.txt", "a")
        transaction_details = {
                'Account Number': account_no,
                'Name': name,
                'Balance': balance,
                'Transaction Type': transaction_type,
                'Amount': amount,
                'Date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        file.write(str(transaction_details) + "\n")
    except Exception as e:
        print("An error occurred while logging the transaction:", e)
