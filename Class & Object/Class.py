# Class 
# A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods. 

# The __init__ method 
# The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object. 

# Example :1

class Myclass(object):
    def show(self):
        print("I am Abhishek")

x=Myclass()
x.show()

# Example :2

class Mobile:
    def __init__(self):
        self.model="Redmi Note 8 Pro"
    
    def show_model(self):
        print("Model: " + self.model)

redmi=Mobile()  #creating object

redmi.model="Iphone 14 Pro Max"
print(redmi.model)   #Accesing Variable outside class

redmi.show_model()


# Example :3

class Laptop:
    def __init__(self,v):
        self.variant=v
    
    def show_variant(self,p):
        print(f"variant:{self.variant} price:{p}")

mi=Laptop("Mi Notebook 14")
print(id(mi))

print(mi.variant)
mi.show_variant(35000)



# Example :4
class PC:
    def __init__(self,v):
        self.variant=v
    
    def show_variant(self,p):
        print(f"variant:{self.variant} price:{p}")

xiaomi=PC("MI Notebook Pro")
xiaomi.show_variant(50000)
print(id(xiaomi))
print()

Macbook=PC("Macbook Pro M1")
Macbook.show_variant(100000)
print(id(Macbook))
