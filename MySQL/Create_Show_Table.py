# Creating Connection:
import mysql.connector
config={
    "user":"root",
    "password":"12345",
    "host":"localhost",
    "database":"python_mysql",
    # "database":"technical_abhi",
    "port":3306
}

try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("Connection established successfully...")
except:
    print("Could not connect to mysql server")

# Creating Tables:
sql='CREATE TABLE  friends(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(25), mobile VARCHAR(20) , city VARCHAR(40))'

myc=conn.cursor()
myc.execute(sql)
myc.close()


# Show Tables :
# sql="SHOW TABLES"
# myc=conn.cursor()
# myc.execute(sql)

# for  t in myc:
#     print(t)

# myc.close()

# Close Connection:
conn.close()
if(conn.is_connected()):
        print("Connection not closed 🐉")
else:
    print("Connection closed successfully",)