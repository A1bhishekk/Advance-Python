
# Instance Method w/o parameter

class Mobile:

    def __init__(self ,m):
        # self.model="Realme X"
        self.model=m
    # instance method
    def show_model(self,p):
        self.price=p
        print(f"Model:{self.model} Price:{self.price}")

redmi=Mobile("Redmi Note 8 Pro")
realme=Mobile("Realme Note 9 Pro Plus")

redmi.show_model(16000)
realme.show_model(20000)


# Accesor /Gettor  Method  
# This method is used to access the state of the object i.e, 
# the data hidden in the object can be accessed from this method.
#  However, this method cannot change the state of the object, 
# it can only access the data hidden. We can name these methods with the word get. 
class Phone:
    def __init__(self):
        self.model="iphone x"


    def get_model(self):
        return self.model


iphone=Phone()
m=iphone.get_model()
print(m)





# Mutator / Setter Method  
#  This method is used to mutate/modify the state of an object i.e,
#  it alters the hidden value of the data variable. 
# It can set the value of a variable instantly to a new value. 
# This method is also called as update method. Moreover, we can name these methods with the word set. 

class Phones:
    def __init__(self):
        self.model="iphone x"


    def set_model(self):
        self.model="iphone 14 pro max"


iphones=Phones()
iphones.set_model()
print(iphones.model)