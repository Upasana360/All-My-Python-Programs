class Circle:
    pi=3.1415
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*Circle.pi*self.radius
p1=Circle(5)
p2=Circle(2)
print(round(p1.circumference()))
print(p2.circumference())


