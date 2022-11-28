import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return f"Point({self.x},{self.y})"

class Triangle:
    def __init__(self, p1, p2, p3):
        if not (isinstance(p1, Point) and isinstance(p2, Point) and isinstance(p3, Point)):
            raise TypeError("Triangle construction requires three Points")
        else:
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
    
    def __str__(self):
        return f'[{self.p1},{self.p2},{self.p3}]'
    
    def __repr__(self):
        return f"Triangle({repr(self.p1)},{repr(self.p2)},{repr(self.p3)}"



def slope(p1, p2):
    if p1.x == p2.x:
        return 'Undefined'
    else:
        return (p1.y - p2.y)/(p1.x - p2.x)

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)



def sides_list(tri):
    return sorted([dist(tri.p1, tri.p2), dist(tri.p2, tri.p3), dist(tri.p3, tri.p1)])

def perimeter(tri):
    return sum(sides_list(tri))

def area(tri):
    s = perimeter(tri)/2
    sides = sides_list(tri)
    return math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))

def is_right(tri, tol = 0.0000001):
    sides = sides_list(tri)
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tol

def is_degen(tri, tol = 0.0000001):
    return area(tri) < tol

def is_congruent(tri1, tri2):
    return sides_list(tri1) == sides_list(tri2)
