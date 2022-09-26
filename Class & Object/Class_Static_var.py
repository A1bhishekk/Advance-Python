# Class variables /Static Variable− 
# Class variables also known as static variables are declared with the static keyword in a class, but outside a method, constructor or a block. There would only be one copy of each class variable per class, regardless of how many objects are created from it.

class Mobile:
    fp="yes"             # class variable

    @classmethod
    def is_fp(cls):
        print(cls.fp)   #Accesing Class Method

realme=Mobile()
print(Mobile.fp)
Mobile.is_fp()


class Phone:
    camera="yes"          #Class Variable

    def __init__(self):
        self.model="Iphone X"   #Instance Variable

    def show_model(self):       #Instance Method
        print("Model :", self.model)  #Accesing instance variable
    
    @classmethod
    def is_camera(cls):         #Class Method
        print("Camera :" ,cls.camera)  #Accesing class variable

redmi=Phone()
print(Phone.camera)
Phone.is_camera()
redmi.show_model()
           

# NameSpace  

class Laptop:
    model="Mi Notebook"   #class namespace


mac=Laptop()
mi=Laptop()   #instance namespace
hp=Laptop()

print(Laptop.model)
print(mac.model)
print(mi.model)
print(hp.model)
Laptop.model = "Mi Notebook Pro"
print(mac.model)
print(mi.model)
print(hp.model)
