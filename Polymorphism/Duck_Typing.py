#DUCK TYPING

class Goat:
    def talk(self):
        print("may may")

class Cat:
    def talk(self):
        print("meow meow")

def myfunction(obj):
    obj.talk()

g=Goat()
myfunction(g)

c=Cat()
myfunction(c)