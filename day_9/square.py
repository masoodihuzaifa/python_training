class Vector:
        def __init__(self, x, y):
                self.x = x
                self.y = y
        def length(self):
                return (self.x ** 2)

v = Vector(3,5)
print v.length()
