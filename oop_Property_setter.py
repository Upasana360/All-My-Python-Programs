#Encapsulation
#datamember+member_fun(in one place)
#Abstraction-hide the complexity from user
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        self.__price=price
        #self.complete_specification=f"{self.brand}{self.model_name}and price is {self._price}"
    def complete_specification(self):
        return f"{self.brand}{self.model_name}and price is {self._price}"
    def make_a_call(self,phone_no):
        print(f"calling{phone_no}.....")
    def full_name(self):
        return f"{self.brand}{self.model_name}"
    def send_msg(self):
        pass
   #@property
    #def complete_specification(self):
        #return f"{self.brand}{self.model_name}and price is {self._price}"
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)
phone1=Phone('nokia','1100',1000)
phone2=Phone('smaetphone','2000',2000)
print(phone1.brand)
print(phone1._price)
print(phone1.make_a_call(9556876464))
phone1.price=-900
print(phone1.price)
phone1._Phone__price=7000
print(phone1._Phone__price)
#print(phone1.complete_specification())
print(phone1.complete_specification())
phone1.price=-700
print(phone1.price)
#print(phone1.__dict__)



