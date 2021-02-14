# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name=brand_name
#         self.model_name=model_name
#         self.price=price
# p1=Laptop("hp","xyz",50000)
# p2=Laptop('dell','yyy',60000)
# print(p1.brand_name)
# print(p2.brand_name)
# print(p1.price)
#oop instance method:
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def fullname(self):
        return self.brand_name+' '+self.model_name
    def is_above(self):
        return self.price>80000
p1=Laptop("hp","xyz",50000)
p2=Laptop('dell','yyy',60000)
print(p1.brand_name)
print(p2.brand_name)
print(p1.price)
print(p1.fullname())
print(Laptop.fullname(p1))
print(p1.is_above())

