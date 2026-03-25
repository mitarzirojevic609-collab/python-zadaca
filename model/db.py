import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12061998",
    database="libary",
    cursorclass=pymysql.cursors.DictCursor
)
if connection.open:
    print("Connected")
else:
    print("Connection failed")
