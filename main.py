from point import Point
from triangle import Triangle

a = Point(0,0)
b = Point(1,1)
c = Point(0,2)
d = Point(2,0)
e = Point(3,1)
f = Point(4,0)
print("Point A =", a)
print("Point B =", b)
print("Point C =", c)
print("Point D =", d)
print("Point E =", e)
print("Point F =", f)

print("\nThe slope of Line AB =", a.slope(b))
print("The slope of Line AC =", a.slope(c))
print("The slope of Line DF =", d.slope(f))
print("The distance between Points E and F is", e.dist(f))
print("The distance between Points D and F is", d.dist(f))

# I normally use lowercase, but that doesn't work with def. LOL.
ABC = Triangle(a, b, c)
DEF = Triangle(d, e, f)
ADF = Triangle(a, d, f)
print("\nTriangle ABC =", ABC)
print("Triangle DEF =", DEF)
print("Triangle ADF =", ADF)

print("\nThe side lengths of Triangle ABC are", ABC.sides_list())
print("The perimeter of Triangle ABC is", ABC.perimeter())
print("The area of Triangle DEF is", DEF.area())
print("The area of Triangle ADF is", ADF.area())

print("\nIs Triangle DEF a right angle?", DEF.is_right())
print("Is Triangle ADF a right angle?", ADF.is_right())
print("Is Triangle ABC degenerate?", ABC.is_degen())
print("Is Triangle ADF degenerate?", ADF.is_degen())
print("Are Triangles ABC and DEF congruent?", ABC.is_congruent(DEF))
print("Are Triangles DEF and ADF congruent?", DEF.is_congruent(ADF))