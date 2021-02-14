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
        

phone1=Phone('nokia','1100',1000)    
smart1=Smartphone('nokia','2300',4000,'4GB','256GB')
smart2=Smartphone2('nokia','2300',4000,'4GB','256GB','16MP')
print(phone1.full_name())
print(smart1.full_name())
print(smart1.model_name)
print(smart1._price)
print(smart1.ram)
print(smart1.external_memory)
# print(help(Smartphone))
print(smart2.backcam)
print(smart2.full_name())
print(isinstance(phone1,Smartphone))
print(issubclass(Phone,Smartphone))
print(issubclass(Smartphone,Phone))