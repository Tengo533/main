class AreaOfShapes:
    def __init__(self, length, height, base, radius):
        self.PI = 3.14159
        self.length = length
        self.height = height
        self.base = base
        self.radius = radius
    
    def rectangle_area(self):
        result = self.length * self.height
        return result
    
    def triangle_area(self):
        result = (self.base * self.height) / 2
        return result
    
    def circle_area(self):
        result = self.PI * (self.radius ** 2)
        return result
    
    def square_area(self):
        result = self.length ** 2
        return result