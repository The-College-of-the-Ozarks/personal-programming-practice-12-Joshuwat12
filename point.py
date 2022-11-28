import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __str__(self):
    return f"({self.x},{self.y})"
    
  def __repr__(self):
    return f"Point({self.x},{self.y})"

  def slope(self, other):
    if self.x == other.x:
      return 'Undefined'
    else:
      return (self.y - other.y)/(self.x - other.x)

  def dist(self, other):
    return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)