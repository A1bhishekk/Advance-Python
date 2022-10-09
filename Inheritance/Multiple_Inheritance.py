# MULTIPLE INHERITANCE 
class Father:
    def __init__(self):
        super().__init__()
        print("Father class constructor")
    def showF(self):
        print("Father class instance method")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother class constructor")
    def showM(self):
        print("Mother class instance method")

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Son class constructor")
    
    def showS(self):
        print("Son class instance method")

s=Son()
s.showM()
s.showF()