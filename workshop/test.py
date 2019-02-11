class Point:
    center = (0,0)
    def __init__(self, x, y):
        self.center=(x,y)
    
p1=Point(3,5)


class Circle(Point):
    r=1
    def __init__(self, p,r):
        super().__init__(p.center[0],p.center[1])
        self.r=r
    def get_area(self):
        return self.r**2*3.14
    def get_perimeter(self):
        return self.r*2*3.14
    def get_center(self):
        return self.center
    def print(self):
        print( 'Circle: ' + str(self.center) + ', r: ' + str(self.r))

p1=Point(0,0)
c1 = Circle(p1, 3) 
print(c1.get_area()) 
print(c1.get_perimeter()) 
print(c1.get_center()) 
c1.print() 
p2 = Point(4, 5) 
c2 = Circle(p2, 1) 
print(c2.get_area()) 
print(c2.get_perimeter())
print(c2.get_center()) 
c2.print()

