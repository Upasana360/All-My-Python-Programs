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
class Smartphone2(Smartphone):
    def __init__(self,brand,model_name,price,ram,external_memory,backcam):
        super().__init__(brand,model_name,price,ram,external_memory)
        self.backcam=backcam
smart2=Smartphone2("nokia","1090",5000,"4GB","256gb","18MP")
print(smart2.backcam)
print(smart2.brand)
#print(help(Smartphone2))
print(smart2.ram)