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

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def as_tuple(self):
        return (self.x, self.y)

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def abs_x(self):
        return abs(self.x)

    def abs_y(self):
        return abs(self.y)

def route_to_vector(route):
    return Vector(route.pos2[0] - route.pos1[0], route.pos2[1] - route.pos1[1])
