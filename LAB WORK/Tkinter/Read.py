from tkinter import *
from Connection import mydb, mycursor


def read():
    root = Tk()

    root.geometry("400x400")
    root.title("View Details")

    # id = Label(root,text="ID",font=("comic",16,"bold"))
    # id.place(x=20,y=50)

    # getid = Entry(root,text="",font=("comic",16,"bold"))
    # getid.place(x=20,y=100)

    # btn = Button(root,text="Get Details",font=("comic",10,"bold"),bg="green")
    # btn.place(x=100,y=150)

    # name = Label(root,text="Name",font=("comic",16,"bold"))
    # name.place(x=20,y=200)

    # getname = Label(root,text="",font=("comic",16,"bold"))
    # getname.place(x=100,y=200)

    # email = Label(root,text="Email",font=("comic",16,"bold"))
    # email.place(x=20,y=250)

    # getemail = Label(root,text="",font=("comic",16,"bold"))
    # getemail.place(x=100,y=250)

    # password = Label(root,text="Password",font=("comic",16,"bold"))
    # password.place(x=20,y=300)

    # getpassword = Label(root,text="",font=("comic",16,"bold"))
    # getpassword.place(x=100,y=300)

    # mobileno = Label(root,text="Mobile No",font=("comic",16,"bold"))
    # mobileno.place(x=20,y=350)

    query = "select * from tkinter2"
    mycursor.execute(query)
        
    data = mycursor.fetchall()
    
    print("DATA FECTHED SUCCESSFULLY")
    all = Label(root,text=data,font=("comic",16,"bold"))
    all.place(x=50,y=100)
    root.mainloop()