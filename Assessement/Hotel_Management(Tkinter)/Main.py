from tkinter import *
from Database_Connection import *
from ShowGuest_list import *
from Checkin import *
from View_Guest import *

# Function to open the Check-In window
def open_checkin():
    new_window = Toplevel(root)
    CheckIn(new_window)
    
# Function to open the View Guest window
def open_viewguest():
    new_window = Toplevel(root)
    ViewGuest(new_window)
    
# Function to open the Check-Out window and display a message
def open_check_out_window():
    checkout_window = Toplevel(root)
    checkout_window.geometry("300x200")
    checkout_window.title("Check Out")

    message_label = Label(checkout_window, text="Check out successfully", font=("Arial", 16))
    message_label.pack(pady=20)

    ok_button = Button(checkout_window, text="OK", font=("Arial", 12), command=checkout_window.destroy)
    ok_button.pack()

# Main function to create the main application window
def main():
    global root
    
    root = Tk()

    root.geometry("1100x650")
    root.title("HOTEL MANAGEMENT")
    
    # Create and pack a canvas for background color
    Can = Canvas(root, bg="pink", height=1200, width=1200)
    Can.pack()

    # Welcome label
    lbl1 = Label(root, text="WELCOME", font=("arial black", 30, "bold"), bg="pink")
    lbl1.place(x=450, y=50)

    # Check-In button
    btn1 = Button(root, text="1.CHECK IN ", font=("arial black", 10, "bold"), height=4, width=40, command=open_checkin)
    btn1.place(x=200, y=120)

    # Show Guest List button
    btn2 = Button(root, text="2.SHOW GUEST LIST ", font=("arial black", 10, "bold"), height=4, width=40, command=Guestlist)
    btn2.place(x=200, y=220)

    # Check-Out button
    btn3 = Button(root, text="3. CHECK OUT", font=("arial black", 10, "bold"), height=4, width=40, command=open_check_out_window)
    btn3.place(x=200, y=320)

    # Get Info of Any Guest button
    btn4 = Button(root, text="4. GET INFO OF ANY GUEST ", font=("arial black", 10, "bold"), height=4, width=40, command=open_viewguest)
    btn4.place(x=200, y=420)

    # Exit button
    btn5 = Button(root, text="5. EXIT ", font=("arial black", 10, "bold"), height=4, width=40, command=quit)
    btn5.place(x=200, y=520)

    # Hotel Management label
    lbl2 = Label(root, text="HOTEL MANAGEMENT ", font=("Bodoni MT Black", 30), bg="pink")
    lbl2.place(x=580, y=150)

    # Python Tkinter label
    lbl3 = Label(root, text="Python Tkinter", font=("Bodoni MT Black", 40), bg="pink")
    lbl3.place(x=620, y=250)

    # GUI label
    lbl3 = Label(root, text="GUI", font=("Bernard MT Condensed", 100), bg="pink")
    lbl3.place(x=730, y=350)

    # Start the main loop of the application
    root.mainloop()
