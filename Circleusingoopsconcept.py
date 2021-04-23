class Circle:
    def __init__(self,radius):
        self.rad=radius
    def getArea(self):
        return 3.14*(self.rad**2)
    def getPerimeter(self):
        return 2*3.14*self.rad

circle1=Circle(3)
print(circle1.getArea())
print(circle1.getPerimeter())