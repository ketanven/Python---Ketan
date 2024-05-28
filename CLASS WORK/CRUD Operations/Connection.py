import pymysql

mydb = pymysql.connect(host = "localhost",user="root",password="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists Crudpython")
mydb.commit()


mydb = pymysql.connect(host = "localhost",user="root",password="",database="Crudpython")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists Crudoperations2(id int primary key Auto_increment,Name varchar(20),Subject varchar(20),Marks int)")
mydb.commit()