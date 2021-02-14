class Person:
    count_instance=0 #cls ,cls attribute
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.F_name=first_name
        self.S_name=last_name
        self.age=age
    @classmethod
    def from_string(cls,string):
        fname,lname,age=string.split(",")
        return cls(fname,lname,age)
    def fullname(self):
        return f"{self.F_name} {self.S_name}"
p1=Person.from_string("harshit,vashitha,24")
p2=Person.from_string("Upasana,Majhi,22")
print(p1.fullname())
print(p2.fullname())



