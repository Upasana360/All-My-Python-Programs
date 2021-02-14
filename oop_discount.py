class Laptop:
    discount_percent=10
    def __init__(self,brand_name,model_name,price):
        print("")
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def discount(self):
        off_price=self.price*(self.discount_percent/100)
        return self.price-off_price
#Laptop.discount_percent=0
a1=Laptop('hp','xyz',60000)
a2=Laptop('hp','xyz',50000)
a3=Laptop('hp','xyz',40000)
a2.discount_percent=20
print(a2.discount())