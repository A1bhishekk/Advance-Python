# Creating Connection:
import pymysql
config={
    "user":"admin",
    "password":"970979120",
    "host":"database-1.cecirdqtsbb3.ap-south-1.rds.amazonaws.com",
    "port":3306
}

# db=pymysql.connect(**config)
# db=pymysql.connect("database-1.cecirdqtsbb3.ap-south-1.rds.amazonaws.com","admin","9709792120","3306")
db=pymysql.connect(host='database-1.cecirdqtsbb3.ap-south-1.rds.amazonaws.com',
                   user='admin',
                   password='9709792120'
                   )
cursor=db.cursor()
print(cursor)
    
