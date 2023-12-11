# used for setting up the django with mysql.

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'rootuser'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("Database setup done.")