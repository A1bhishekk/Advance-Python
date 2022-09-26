
# CONSTRUCTOR IN INHERITANCE
class Father:
    def __init__(self,m):
        self.money=m
        print("Father class constructor called")
    
    def show(self):
        print("Parent class instance Method",self.money)

class Son(Father):
    def disp(self,p):
        print("Child class instance Method",self.money+p)

s=Son(10000)
print(s.money)
s.show()
s.disp(5000)