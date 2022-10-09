# Hierarchical Inheritance
'''
Hierarchical inheritance describes a situation in which a parent 
class is inherited by multiple subclasses. A type of inheritance 
in which more than one class is inherited from a single parent or 
base class is known as hierarchical inheritance.

'''
class Father:
    
    def showF(self):
        print("Father class instance method")

class Son(Father):
    
    def showS(self):
        print("Son class instance method")

class Daughter(Father):
    
    def showD(self):
        print("Daughter class instance method")

s=Son()
s.showF()
s.showS()
s.showD()

