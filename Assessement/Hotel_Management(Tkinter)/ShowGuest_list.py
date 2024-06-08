from tkinter import *
from Database_Connection import *

# Function to fetch all guest records from the database
def Showguest():
    mycursor.execute("SELECT * FROM bookings")  # Execute SQL query to select all records from the bookings table
    print("Showing Guest List")
    return mycursor.fetchall()  # Fetch and return all records

# Function to display the guest list in a new window
def Guestlist():
    guest_list = Showguest()  # Get the guest list from the database

    root = Tk()  # Create a new Tkinter window
    root.geometry("1000x1200")  # Set the window size
    root.title("Guest List")  # Set the window title
    
    # Title label for the window
    title = Label(root, text="YOU CLICKED ON : GUEST LIST", font=("arial", 15, "bold"))
    title.place(x=100, y=20)

    # Main heading for the guest list
    Label(root, text="Guest List", font=("arial", 20, "bold")).pack(pady=50)

    # Text area to display the guest information
    text_area = Text(root, font=("arial", 12))
    text_area.pack(expand=1, fill=BOTH, padx=20, pady=20)

    # Check if the guest list is not empty and insert guest information into the text area
    if guest_list:
        for guest in guest_list:
            guest_info = f"ID: {guest[0]}, Name: {guest[1]}, Address: {guest[2]}, Number: {guest[3]}, Days: {guest[4]}, Room Type: {guest[5]}, Payment Method: {guest[6]}\n"
            text_area.insert(END, guest_info)
    else:
        # If no guests are found, display a message
        text_area.insert(END, "No guests found.")

    root.mainloop()  # Run the Tkinter event loop
