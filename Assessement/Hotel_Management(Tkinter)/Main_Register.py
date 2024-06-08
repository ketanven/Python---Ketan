from tkinter import *
from Main import *
from Database_Connection import mycursor, mydb

# Function to handle form submission
def submit():
    # Check if all required fields are filled
    if not eName.get() or not eContact.get() or not eEmail.get() or (gender.get() != 1 and gender.get() != 2) or city.get() == "Select" or state.get() == "Select":
        error_msg.config(text="All fields are required!", fg="red")  # Show error message
    else:
        error_msg.config(text="Submitted successfully!", fg="green")  # Show success message
        
        # SQL query to insert form data into the database
        sql = "INSERT INTO registration (name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (eName.get(), eContact.get(), eEmail.get(), "Male" if gender.get() == 1 else "Female", city.get(), state.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"{mycursor.rowcount} record inserted.")  # Print number of records inserted
        
        # Clear form fields
        eName.delete(0, END)
        eContact.delete(0, END)
        eEmail.delete(0, END)
        gender.set(0)
        city.set("Select")
        state.set("Select")
        
        # Close the form and open the main application
        root.destroy()
        open_main_app()

# Function to open the main application
def open_main_app():
    main()

# Set up the main window
root = Tk()
root.geometry("500x500")
root.title("Registration Form")

# Label for form title
lbl = Label(root, text="Please enter details below", bg="yellow", font=("arial", 12, "bold"), width=50)
lbl.place(x=0, y=0)

# Label and entry for Name
Name = Label(root, text="Name * ", font=("arial", 16, "bold"))
Name.place(x=10, y=50)

eName = Entry(root, font=("arial", 16, "bold"))
eName.place(x=120, y=55)

# Label and entry for Contact
Contact = Label(root, text="Contact * ", font=("arial", 16, "bold"))
Contact.place(x=10, y=100)

eContact = Entry(root, font=("arial", 16, "bold"))
eContact.place(x=120, y=110)

# Label and entry for Email
Email = Label(root, text="Email * ", font=("arial", 16, "bold"))
Email.place(x=10, y=160)

eEmail = Entry(root, font=("arial", 16, "bold"))
eEmail.place(x=120, y=170)

# Label for Gender
Gender = Label(root, text="Gender * ", font=("arial", 16, "bold"))
Gender.place(x=10, y=220)

# Radio buttons for Gender selection
gender = IntVar()
RGenderMale = Radiobutton(root, text="Male", font=("arial", 16, "bold"), value=1, variable=gender)
RGenderMale.place(x=150, y=220)

RGenderFemale = Radiobutton(root, text="Female", font=("arial", 16, "bold"), value=2, variable=gender)
RGenderFemale.place(x=250, y=220)

# Label and dropdown for City selection
City = Label(root, text="City *", font=("arial", 16, "bold"))
City.place(x=10, y=280)

city = StringVar()
city.set("Select")
ECity = OptionMenu(root, city, "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", "Bharuch")
ECity.config(width=35)
ECity.place(x=120, y=280)

# Label and dropdown for State selection
State = Label(root, text="State *", font=("arial", 16, "bold"))
State.place(x=10, y=340)

state = StringVar()
state.set("Select")
EState = OptionMenu(root, state, "Gujarat", "Delhi", "Tamil Nadu", "Kerala", "Rajasthan", "Uttarakhand")
EState.config(width=35)
EState.place(x=120, y=340)

# Label to show error or success messages
error_msg = Label(root, text="", font=("arial", 12, "bold"))
error_msg.place(x=10, y=400)

# Submit button
submit_btn = Button(root, text="Register", bg="yellow", font=("arial", 16, "bold"), command=submit)
submit_btn.place(x=200, y=450)

# Run the main loop
root.mainloop()
