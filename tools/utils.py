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