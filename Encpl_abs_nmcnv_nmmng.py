#Encapsulation
#datamember+member_fun(in one place)
#Abstraction-hide the complexity from user
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.__price=price
    def make_a_call(self,phone_no):
        print(f"calling{phone_no}.....")
    def full_name(self):
        return f"{self.brand}{self.model_name}"
    def send_msg(self):
        pass
phone1=Phone('nokia','1100',1000)
phone2=Phone('smaetphone','2000',2000)
print(phone1.brand)
print(phone1._price)
print(phone1.make_a_call(9556876464))
phone1._price=6000
print(phone1._price)
phone1._Phone__price=7000
print(phone1._Phone__price)
#print(phone1.__dict__)



