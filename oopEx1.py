class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def discount(self,n):
        off_price=self.price*(n/100)
        return self.price-off_price
a1=Laptop('hp','xyz',60000)
print(a1.discount(10))