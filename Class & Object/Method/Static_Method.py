

# STATIC METHOD
# A static method does not receive an implicit first argument. 
# A static method is also a method that is bound to the class 
# and not the object of the class. This method can’t access or modify 
# the class state. It is present in a class because 
# it makes sense for the method to be present in class.

class Mobile:
    ram="128gb"
    @staticmethod
    def phone(m,p):
        print(f"Model : {m} Price: {p}")
        print(Mobile.ram)

iphone=Mobile()

Mobile.phone("Iphone 14 Pro Max",140000)