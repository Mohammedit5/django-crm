import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="Mohammed_it5"
)


cursorObject = dataBase.cursor()        
cursorObject.execute("CREATE DATABASE dcrm_db")

print("Database created successfully!")