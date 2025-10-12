import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Aklesiya",          # change this
    password="Strongdudu0900", # change this
    database="alx_book_store"    # change this
)

print("Connected to:", mydb.get_server_info())

mydb.close()
