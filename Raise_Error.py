
#----------------------------------------------------------------------------------------
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError("you hv to define thismtd in subclsses also")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return "bhow bhow"
       
doggy=Dog('bonny','pug')
print(doggy.sound())   
