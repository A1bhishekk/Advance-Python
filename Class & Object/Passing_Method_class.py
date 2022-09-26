# Passing Member of one class to another class

class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    
    def show(self):
        print("Student: " + self.name)
        print("Roll: " + self.roll)

class User:
    @staticmethod
    def users(s):
        print("User: " + s.name)
        print("Roll No: " + s.roll)

stu=Student("Abhishek","0177CS191010")

User.users(stu)
stu.show()