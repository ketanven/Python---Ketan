from tkinter import *
from Database_Connection import mycursor, mydb

# Guest class to represent guest details
class Guest:
    def __init__(self, name, address, number, days):
        self._name = name
        self._address = address
        self._number = number
        self._days = days

    # Property for name
    @property
    def name(self):
        return self._name

    # Property for address
    @property
    def address(self):
        return self._address

    # Property for number
    @property
    def number(self):
        return self._number

    # Property for days
    @property
    def days(self):
        return self._days

# Customer class inheriting from Guest class
class Customer(Guest):
    def __init__(self, name, address, number, days):
        super().__init__(name, address, number, days)
        self.__balance = 0

    # Property for balance
    @property
    def balance(self):
        return self.__balance

    # Setter for balance with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

# CheckIn class to handle the check-in process
class CheckIn:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x800")
        self.root.title("Hotel Management System")
        Can = Canvas(self.root, bg="lightblue", height=1900, width=1350)
        Can.pack()

        # Variables for room type and payment method
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()

        self.init_ui()

    # Method to initialize the user interface
    def init_ui(self):
        title = Label(self.root, bg="lightblue", text="YOU CLICKED ON : CHECK IN", font=("arial", 25, "bold"))
        title.place(x=400, y=20)

        # Name input field
        Label(self.root, text="ENTER YOUR NAME", bg="lightblue", font=("arial", 20)).place(x=150, y=100)
        self.eName = Entry(self.root, font=("arial", 20))
        self.eName.place(x=600, y=100)
        Button(self.root, text="OK",bg="orange", font=("arial", 15), command=self.validate_name).place(x=920, y=100)

        # Address input field
        Label(self.root, text="ENTER YOUR ADDRESS", bg="lightblue", font=("arial", 20)).place(x=150, y=160)
        self.eAddress = Entry(self.root, font=("arial", 20))
        self.eAddress.place(x=600, y=160)
        Button(self.root, text="OK",bg="orange", font=("arial", 15), command=self.validate_address).place(x=920, y=160)

        # Number input field
        Label(self.root, text="ENTER YOUR NUMBER", bg="lightblue", font=("arial", 20)).place(x=150, y=220)
        self.eNumber = Entry(self.root, font=("arial", 20))
        self.eNumber.place(x=600, y=220)
        Button(self.root, text="OK",bg="orange", font=("arial", 15), command=self.validate_number).place(x=920, y=220)

        # Number of days input field
        Label(self.root, text="NUMBER OF DAYS", bg="lightblue", font=("arial", 20)).place(x=150, y=280)
        self.eDays = Entry(self.root, font=("arial", 20))
        self.eDays.place(x=600, y=280)
        Button(self.root, text="OK",bg="orange", font=("arial", 15), command=self.validate_days).place(x=920, y=280)

        # Room type selection
        Label(self.root, text="CHOOSE YOUR ROOM", bg="lightblue", font=("arial", 20)).place(x=150, y=340)
        Checkbutton(self.root, text="DELUXE",bg="lightblue", variable=self.var1, font=("arial", 20)).place(x=600, y=340)
        Checkbutton(self.root, text="FULL DELUXE",bg="lightblue", variable=self.var2, font=("arial", 20)).place(x=750, y=340)
        Checkbutton(self.root, text="GENERAL",bg="lightblue", variable=self.var3, font=("arial", 20)).place(x=600, y=400)
        Checkbutton(self.root, text="JOINT",bg="lightblue", variable=self.var4, font=("arial", 20)).place(x=750, y=400)

        # Payment method selection
        Label(self.root, text="CHOOSE PAYMENT METHOD",bg="lightblue", font=("arial", 20)).place(x=150, y=460)
        Checkbutton(self.root, text="By cash",bg="lightblue", variable=self.var5, font=("arial", 20)).place(x=600, y=460)
        Checkbutton(self.root,bg="lightblue", text="By credit/debit card", variable=self.var6, font=("arial", 20)).place(x=750, y=460)

        # Submit button
        Button(self.root,bg="orange", text="SUBMIT", font=("arial", 20), command=self.submit).place(x=600, y=520)

        # Message label to display status messages
        self.message_label = Label(self.root,bg="red",fg="white", text="", font=("arial", 15,"bold"), justify="left")
        self.message_label.place(x=150, y=580)

    # Method to validate name input
    def validate_name(self):
        name = self.eName.get()
        if not name:
            self.message_label.config(text="Name has not been inputted")
        else:
            self.message_label.config(text="Name inputted successfully")

    # Method to validate address input
    def validate_address(self):
        address = self.eAddress.get()
        if not address:
            self.message_label.config(text="Address has not been inputted")
        else:
            self.message_label.config(text="Address inputted successfully")

    # Method to validate number input
    def validate_number(self):
        number = self.eNumber.get()
        if not number or not number.isdigit():
            self.message_label.config(text="Mobile number has not been inputted or is invalid")
        else:
            self.message_label.config(text="Mobile number inputted successfully")

    # Method to validate days input
    def validate_days(self):
        days = self.eDays.get()
        if not days or not days.isdigit():
            self.message_label.config(text="Number of days has not been inputted or is invalid")
        else:
            self.message_label.config(text="Number of days inputted successfully")

    # Method to handle form submission
    def submit(self):
        name = self.eName.get()
        address = self.eAddress.get()
        number = self.eNumber.get()
        days = self.eDays.get()

        message = ""

        # Check if all fields are filled
        if not name or not address or not number or not days:
            message += "Please input all fields"
        else:
            customer = Customer(name, address, number, days)
            message += f"Name = {customer.name} : Inputted Successfully\nAddress = {customer.address} : Inputted Successfully\nNumber = {customer.number} : Inputted Successfully\nDays = {customer.days} : Inputted Successfully\n"

            # Room type selection
            room_type = ""
            if self.var1.get() == 1:
                room_type += "Deluxe "
            if self.var2.get() == 1:
                room_type += "Full Deluxe "
            if self.var3.get() == 1:
                room_type += "General "
            if self.var4.get() == 1:
                room_type += "Joint "

            # Payment method selection
            payment_method = ""
            if self.var5.get() == 1:
                payment_method = "By cash"
            if self.var6.get() == 1:
                payment_method = "By credit/debit card"

            if not room_type:
                message += "Room type has not been selected\n"
            if not payment_method:
                message += "Payment method has not been selected\n"

            message += f"Room Type: {room_type}\nPayment: {payment_method}"

            # Insert record into database
            sql = "INSERT INTO bookings (name, address, number, days, room_type, payment_method) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (customer.name, customer.address, customer.number, customer.days, room_type, payment_method)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"{mycursor.rowcount} record inserted.")
            
        # Clear input fields after submission
        self.eName.delete(0, END)
        self.eAddress.delete(0, END)
        self.eNumber.delete(0, END)
        self.eDays.delete(0, END)
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.message_label.config(text=message)
