from Connection import mydb, mycursor

from tkinter import *

def create():
    window = Tk()
    window.geometry("500x500")
    window.title("Tkinter Program")

    lbl1 = Label(window, text="ID", font=("comic", 16, "bold"))
    lbl1.place(x=20, y=50)

    lbl2 = Label(window, text="Name", font=("comic", 16, "bold"))
    lbl2.place(x=20, y=100)

    lbl3 = Label(window, text="Email", font=("comic", 16, "bold"))
    lbl3.place(x=20, y=150)

    lbl4 = Label(window, text="Password", font=("comic", 16, "bold"))
    lbl4.place(x=20, y=200)

    lbl5 = Label(window, text="Mobile No", font=("comic", 16, "bold"))
    lbl5.place(x=20, y=250)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()

    ent1 = Entry(window, bg="yellow", fg="red", width=10, textvariable=var1)
    ent1.place(x=180, y=50)

    ent2 = Entry(window, bg="yellow", fg="red", width=25, textvariable=var2)
    ent2.place(x=180, y=100)

    ent3 = Entry(window, bg="yellow", fg="red", width=25, textvariable=var3)
    ent3.place(x=180, y=150)

    ent4 = Entry(window, bg="yellow", fg="red", width=25, textvariable=var4)
    ent4.place(x=180, y=200)

    ent5 = Entry(window, bg="yellow", fg="red", width=25, textvariable=var5)
    ent5.place(x=180, y=250)

    def add():
        Name = str(var2.get())
        Email = str(var3.get())
        Password = str(var4.get())
        MobileNo = str(var5.get())

        # Using parameterized query to insert data
        query = "INSERT INTO tkinter2 (Name, Email, Password, MobileNo) VALUES ('%s', '%s', '%s', '%s')"
        args = (Name, Email, Password, MobileNo)

        mycursor.execute(query % args)
        mydb.commit()
        print("DATA INSERTED SUCCESSFULLY")
        window.destroy()  # Close the create window after inserting data

    btn = Button(window, text="Add", command=add, font=("comic", 10, "bold"), bg="green", height=2, width=10)
    btn.place(x=190, y=320)

    window.mainloop()