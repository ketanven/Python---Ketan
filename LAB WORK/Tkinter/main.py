from tkinter import *
from Create import *
from Read import *

root = Tk()

root.geometry("500x500")
root.title("Tkinter Program")

lbl = Label(root, text="WELCOME TO CRUD OPERATIONS", font=("comic", 20), bg="red", fg="white")
lbl.place(x=20, y=50)

btn1 = Button(root, text="Create", bg="yellow", height=2, width=10, font=("comic", 12, "bold"), command=create)
btn1.place(x=200, y=120)

btn2 = Button(root, text="Read", bg="yellow", height=2, width=10, font=("comic", 12, "bold"),command=read)
btn2.place(x=200, y=190)

btn3 = Button(root, text="Update", bg="yellow", height=2, width=10, font=("comic", 12, "bold"))
btn3.place(x=200, y=260)

btn4 = Button(root, text="Delete", bg="yellow", height=2, width=10, font=("comic", 12, "bold"))
btn4.place(x=200, y=330)

btn5 = Button(root, text="Exit", bg="yellow", height=2, width=10, font=("comic", 12, "bold"), command=root.quit)
btn5.place(x=200, y=400)

root.mainloop()
