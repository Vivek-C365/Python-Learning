import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='admin', host='localhost', database='sample')

cursor = conn.cursor()