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