class Mobile:
    def __init__(self,name):
        self.name=name
class MobileStore:
    def __init__(self):
        self.mobiles=[]
    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new_mobile should be object of mobile cls")
oneplus=Mobile('one plus6')
obj=Mobile("nokia")
samsung='samsung galaxys8'
mobostore=MobileStore()
#print(mobostore.mobiles)
mobostore.add_mobile(oneplus)
mobo_phone=mobostore.mobiles
print(mobo_phone[0].name)
mobostore.add_mobile(obj)
mobo_phone1=mobostore.mobiles
print(mobo_phone1[1].name)


