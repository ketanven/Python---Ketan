import pymysql

# Establish the initial connection to create the database
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

# Create the database if it does not exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS HotelManagement")
mydb.commit()

print("Connected to MySQL database and created HotelManagement database!")

# Reconnect to the newly created database
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="HotelManagement"
)
mycursor = mydb.cursor()

# Create the bookings table if it does not exist
mycursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    number VARCHAR(255),
    days INT,
    room_type VARCHAR(255),
    payment_method VARCHAR(255)
)
""")
print("CheckIN Table created successfully!")
mydb.commit()

# Create the registration table if it does not exist
mycursor.execute("""
CREATE TABLE IF NOT EXISTS registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL
)
""")
print("Registration Table created successfully!")
mydb.commit()
