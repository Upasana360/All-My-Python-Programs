class Laptop:
    discount_percent=10
    count=0
    def __init__(self,brand_name,model_name,price):
        Laptop.count+=1
        print(f"instance is called{Laptop.count}time")
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    def discount(self):
        off_price=self.price*(self.discount_percent/100)
        return self.price-off_price
    @classmethod
    def count_instance(cls):
        return f"you have created {cls.count} instances of laptop class"
        #oop static mtd
    @staticmethod
    #here we dont need to pass any kind of argument
    def hello():
        print('hello, static mtd is called')



#Laptop.discount_percent=0
a1=Laptop('hp','xyz',60000)
a2=Laptop('hp','xyz',50000)
a3=Laptop('hp','xyz',40000)
print(Laptop.count)
print(Laptop.count_instance())
Laptop.hello()

