# Creating Connection:
import mysql.connector
config={
    "user":"root",
    "password":"12345",
    "host":"localhost",
    "database":"python_mysql",
    "port":3306
}

try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("Connection established successfully...")
except:
    print("Could not connect to mysql server")

# Insert Data into Table:
sql='DELETE FROM friends WHERE id=7'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,"Row deleted successfully")
except:
    conn.rollback()
    print("Unable to Delete")

myc.close()

# Close Connection:
conn.close()
if(conn.is_connected()):
        print("Connection not closed 🐉")
else:
    print("Connection closed successfully",)