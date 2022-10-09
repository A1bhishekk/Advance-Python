# Creating Connection:
import mysql.connector
config={
    "user":"root",
    "password":"12345",
    "host":"localhost",
    "port":3306
}

try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("Connection established successfully...")
except:
    print("Could not connect to mysql server")


# Close Connection:
conn.close()
if(conn.is_connected()):
        print("Connection not closed 🐉")
else:
    print("Connection closed successfully",)
