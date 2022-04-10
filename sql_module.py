import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="testdatabase"
)
mycursor = db.cursor()