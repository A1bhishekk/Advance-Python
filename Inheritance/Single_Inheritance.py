# SINGLE INHERITANCE 
class Father:
    money=1000
    def show(self):
        print("parent class instance method")

    @classmethod
    def showmoney(cls):
        print("parent class class method ",cls.money)

    @staticmethod
    def stat(n):
        print("parent class static method",n)


class Son(Father):
    def disp(self):
        print("child class instance method")

s=Son()
s.disp()
s.show()
s.showmoney()
s.stat("good")
print(s.money)

