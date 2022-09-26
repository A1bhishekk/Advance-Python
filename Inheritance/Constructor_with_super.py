# CONSTRUCTOR WITH SUPER KEYWORD 
class Father:
    def __init__(self,r):
        self.money=r
        print("Father Class Constructor")

    def show(self):
        print("Father class instance method",self.money)

class Son(Father):
    def __init__(self,m,n):
        super().__init__(m)
        self.balance=n
        self.car="BMW"
        print("Son Class Constructor")

    def disp(self,p):
        print("Son class instance method")
        print("Money:",self.money)
        print("Balane:",self.balance)
        print("Car:",self.car)
        print("Price:",p)

s=Son(1000,100000)
s.show()
print(s.money)
print(s.car)
s.disp(10000000)