

class Rectangle:

   def __init__(self, height, width):
      self._height = height
      self._width = width

   def height(self):
      print("Height of the Rectangle")
      pass

rectangle = Rectangle(3,4)

print("Width ",rectangle._width)
print("Height ",rectangle._height)

rectangle.height = 5

print("Height ",rectangle.height)

