import math

class Circle:
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return math.pi * self.radius ** 2

aCircle = Circle(3)
print(round(aCircle.area(), 2))