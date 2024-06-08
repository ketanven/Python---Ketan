import pymysql

# Establish connection to the MySQL server
mydb = pymysql.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

# Create the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS tkinter")
mydb.commit()

# Reconnect to the created database
mydb = pymysql.connect(host="localhost", user="root", password="", database="tkinter")
mycursor = mydb.cursor()

# Create the table if it doesn't exist
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS tkinter2 (
        id INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(20),
        Email VARCHAR(20),
        Password VARCHAR(20),
        MobileNo BIGINT
    )
""")
mydb.commit()
