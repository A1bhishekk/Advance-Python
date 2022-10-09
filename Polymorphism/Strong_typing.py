#STRONG TYPING

class Goat:
    def talk(self):
        print("may may")

class Cat:
    def talk(self):
        print("meow meow")

class Eagle:
    def fly(self):
        print("Eagles fly in the air") 

def myfunction(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'fly'):
        obj.fly()
    else:
        print("object method not found")

g=Goat()
myfunction(g)

c=Cat()
myfunction(c)

e=Eagle()
myfunction(e)