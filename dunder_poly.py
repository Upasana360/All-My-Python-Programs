class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        self.__price=price
    def complete_specification(self):
        return f"{self.brand}{self.model_name}and price is {self._price}"
    def make_a_call(self,phone_no):
        print(f"calling{phone_no}.....")
    def full_name(self):
        return f"{self.brand}{self.model_name}"
    def __repr__(self):
        return f"phone(\'{self.model_name}\',{self.brand}\')"
    def __str__(self):
        return f"{self._price}\t{self.brand}"
    def __len__(self):
        return(len(self.brand))
    def __mul__(self,other):
        return self._price * other._price
class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,external_memory):
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.external_memory=external_memory
    def full_name(self):
        return f"{self.brand}{self.model_name}and price is {self._price}"
class Smartphone2(Smartphone):
    def __init__(self,brand,model_name,price,ram,external_memory,backcam):
        super().__init__(brand,model_name,price,ram,external_memory)
        self.backcam=backcam
my_phone=Phone("nokiaa","1100",2000)
my_phone2=Phone("nokiaa","1100",6000)
print(my_phone)#it will return the address
print(str(my_phone))
print(repr(my_phone))
print(len(my_phone))
#Operator overloading
print(my_phone*my_phone2)
#polymorphism
#polymorphism is same same as operator overloading
