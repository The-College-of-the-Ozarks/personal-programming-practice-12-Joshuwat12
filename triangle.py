import math
from point import Point

class Triangle:
  def __init__(self, p1, p2, p3):
    if not (isinstance(p1, Point) and isinstance(p2, Point) and isinstance(p3, Point)):
      raise TypeError("selfangle construction requires three Points")
    else:
      self.p1 = p1
      self.p2 = p2
      self.p3 = p3
    
  def __str__(self):
    return f'[{self.p1},{self.p2},{self.p3}]'
    
  def __repr__(self):
    return f"selfangle({repr(self.p1)},{repr(self.p2)},{repr(self.p3)}"

  def sides_list(self):
    return sorted([self.p1.dist(self.p2), self.p2.dist(self.p3), self.p3.dist(self.p1)])

  def perimeter(self):
    return sum(self.sides_list())

  def area(self):
    s = self.perimeter()/2
    sides = self.sides_list()
    return math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))

  def is_right(self, tol = 0.0000001):
    sides = self.sides_list()
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tol

  def is_degen(self, tol = 0.0000001):
    return self.area() < tol

  def is_congruent(self, other):
    return self.sides_list() == other.sides_list()