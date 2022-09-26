
# Nested / Inner Class
class Army:                #outer class
    def __init__(self):
        self.name ="Abhishek"
        self.gn=self.Gun()       #inner class object
    
    def show(self):
        print("Name : " + self.name)
    

    class Gun:            #inner class
        def __init__(self):
            self.name="Ak-47"
            self.capacity="47"
        
        def disp(self):
            print("Gun Name : " + self.name)
            print("Capacity : " + self.capacity)

a=Army()
print(a.name)
a.show()

print(a.gn.name)
# g=a.gn
g=Army().Gun()
print(g.name)
g.disp()