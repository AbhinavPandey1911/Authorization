import mysql.connector
con=mysql.connector.connect(user='root',password='abhinav1234',host='localhost',database='world')
if con.is_connected():
     print("Connection Successfull")