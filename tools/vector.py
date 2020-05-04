from tools.utils import Point

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def abs_x(self):
        return abs(self.x)

    def abs_y(self):
        return abs(self.y)