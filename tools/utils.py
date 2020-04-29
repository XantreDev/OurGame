def degree_editor(angle):
    if angle < 0:
        return (360 - angle)
    elif angle > 360:
        return (angle - 360)
    return angle