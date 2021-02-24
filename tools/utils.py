from levels.level.lvl1_field import Field
from random import randrange
import settings

def heuristic(a, b):
    return abs(a[0]- b[0]) + abs(a[1] - b[1])

def degree_editor(angle):
    if angle < 0:
        return (360 - angle)
    elif angle > 360:
        return (angle - 360)
    return angle

def side_collide(obj, points):
        c = 0
        for point in points:
            c += int(obj.collidepoint(point))
        return (c >= 2)

def spawn_generator():
    i = randrange(1, len(Field)-2)
    j = randrange(1, len(Field[0])-2)
    
    print(i, j)
    
    while Field[i][j] == -1:
        i = randrange(1, len(Field)-2)
        j = randrange(1, len(Field[0])-2)
    
    return (j * settings.precision, i * settings.precision)

def comprasion(f_point, s_point):
    x1, y1 = f_point
    x2, y2 = s_point
    delta = abs(x1-x2) + abs(y1-y2)
    if delta < settings.to_comprasion:
        pass
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def as_tuple(self):
        return (self.x, self.y)
        
    def __mul__(self, other: int):
        self.x *= other
        self.y *= other
        return self
    
    def __truediv__(self, other: int):
        self.x /= other
        self.y /= other
        return self

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def abs_x(self):
        return abs(self.x)

    def abs_y(self):
        return abs(self.y)

    

def route_to_vector(route):
    return Vector(route.pos2[0] - route.pos1[0], route.pos2[1] - route.pos1[1])
