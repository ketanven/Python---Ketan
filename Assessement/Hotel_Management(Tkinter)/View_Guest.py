from tkinter import *
from Database_Connection import mycursor

# Class to create the View Guest window
class ViewGuest:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x500")
        self.root.title("Hotel Management System")
        
        self.init_ui()  # Initialize the user interface
        
    def init_ui(self):
        # Create and pack a canvas for background color
        Can = Canvas(self.root, bg="pink", height=1900, width=1350)
        Can.pack()

        # Title label
        title = Label(self.root, text="YOU CLICKED ON : VIEW GUEST", bg="pink", font=("arial", 25, "bold"))
        title.place(x=400, y=20)

        # Label for guest name entry
        Label(self.root, text="ENTER GUEST NAME", bg="pink", font=("arial", 20)).place(x=150, y=100)

        # Entry widget for guest name
        self.eName = Entry(self.root, font=("arial", 20))
        self.eName.place(x=600, y=100)

        # Search button
        Button(self.root, text="Search", bg="green", fg="white", font=("arial", 15), command=self.show).place(x=950, y=98)

        # Text area to display guest information
        self.text_area = Text(self.root, font=("arial", 12), width=50, height=8)
        self.text_area.place(x=420, y=200)
        
    def show(self):
        # Get the guest name from the entry widget
        name = self.eName.get()
        query = "SELECT * FROM bookings WHERE name = '%s'"
        args = (name,)

        # Execute the query
        mycursor.execute(query % args)
        results = mycursor.fetchall()
        
        # Clear the text area before displaying new results
        self.text_area.delete(1.0, END)
        
        if results:
            # Display each guest's information in the text area
            for guest in results:
                guest_info = f"ID : {guest[0]}\nName : {guest[1]}\nAddress : {guest[2]}\nNumber : {guest[3]}\nDays : {guest[4]}\nRoom Type : {guest[5]}\nPayment Method : {guest[6]}\n"
                self.text_area.insert(END, guest_info)
        else:
            # Display a message if no guests are found
            self.text_area.insert(END, "No guests found.")
        
        print("DATA FETCHED SUCCESSFULLY")
