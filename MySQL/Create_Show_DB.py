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


# CREATE DATABASE  
# sql="CREATE DATABASE PYTHON_MYSQL"
# myc=conn.cursor()
# myc.execute(sql)
# myc.close()


# SHOW DATABASE 
sql="SHOW DATABASES"
myc=conn.cursor()
myc.execute(sql)

for d in myc:
    print(d)

myc.close()

conn.close()