
class Mobile:
    def __init__(self):
        self.model="Redmi Note 8 Pro"   #instance variable
    
    def show_model(self):               #instance method
        print("Model: " + self.model)   #access instance Variable

redmi=Mobile()  #creating object
iphone=Mobile() 

redmi.model="Iphone 14 Pro Max"
print(redmi.model)   #Accesing Variable outside class
print(iphone.model)

redmi.show_model()