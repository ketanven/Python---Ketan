from Connection import *

while True:
    menu = """
    Press 1 : For Insert Data
    Press 2 : For Read Data
    Press 3 : For Update Data
    Press 4 : For Delete Data
    Press 5 : For Exit
    
"""
    print(menu)
    choice = int(input("ENTER YOUR CHOICE =  "))
    
    if choice  == 1:
        print()
        print("LET'S INSERT A DATA")
        print()
        
        name = input("ENTER YOUR NAME = ")
        print()
        subject = input("ENTER YOUR SUBJECT = ")
        print()
        marks = int(input("ENTER YOUR TOTAL MARKS = "))
        print()
        
        query = "insert into Crudoperations2(name,subject,marks) values('%s','%s','%s')"
        
        args = (name,subject,marks)
        
        mycursor.execute(query % args)
        mydb.commit()
        print("DATA INSERTED SUCCESSFULLY")
    
    elif choice == 2:
        print()
        query = "select * from Crudoperations2"
        mycursor.execute(query)
        
        data = mycursor.fetchall()
        print(data)
        print("DATA FECTHED SUCCESSFULLY")
    
    elif choice == 3:
        print()
        id = int(input("ENTER THE ID  = "))
        print()
        name = input("ENTER YOUR NAME = ")
        print()
        subject = input("ENTER YOUR SUBJECT = ")
        print()
        marks = int(input("ENTER YOUR MARKS = "))
        print()
        
        query = "update Crudoperations2 set name = '%s',subject = '%s',marks = '%s' where id = '%s'" 
        args = (name,subject,marks,id)
        
        mycursor.execute(query % args)
        mydb.commit()
        print("DATA UPDATED SUCCESSFULLY")
    
    elif choice == 4:
        print()
        id = int(input("ENTER THE ID = "))
        query = "delete from Crudoperations2 where id = '%s'"
        args = (id)
        
        mycursor.execute(query % args)
        mydb.commit()
        print("DATA DELETED SUCCESSFULLY")
        
    elif choice ==5:
        print()
        print("THANKS")
        break
    else:
        print()
        print("*****EXITING*****")
        break
        