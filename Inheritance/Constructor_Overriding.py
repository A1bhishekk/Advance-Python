# CONSTRUCTOR OVERRIDING

'''
Python constructor overriding mean one method will overrides the other.
The parent class and child class both have the constructor and the child 
will override the parent constructor.

'''

class Father:
    def __init__(self):
        self.money=1000
        print("Father Class Constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def __init__(self,m):
        self.money=m
        self.car="BMW"
        print("Son Class Constructor")

    def disp(self,p):
        print("Son class instance method")
        print("Money:",self.money)
        print("Car:",self.car)
        print("Price:",p)

s=Son(100000)
print(s.money)
print(s.car)
s.disp(10000000)