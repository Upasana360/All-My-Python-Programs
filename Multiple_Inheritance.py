class A:
    def class_a_mtd(self):
        return "I am just a cls A mtd"
    def hello(self):
        return "hello i\'m from cls A"
class B:
    def class_b_mtd(self):
        return "I am just a cls B mtd"
    def hello(self):
        return "hello i\'m from cls B"
class C(B,A):
    pass
instance_c=C()
print(instance_c.class_a_mtd())
print(instance_c.class_b_mtd())
print(instance_c.hello())
