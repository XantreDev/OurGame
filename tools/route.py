import pygame
from tools.vector import Vector

class Route:
    def __init__(self):
        self.pos1 = (0, 0)
        self.pos2 = (0, 0)
    
    def update(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
    
    def side_collide(self, obj, points):
        c = 0
        for point in points:
            c += int(obj.collidepoint(point))
        return (c>=2)
            
    def collide(self, rect, obj, vector): # TODO: refactor
        abs_shift_x = abs(vector.x)
        abs_shift_y = abs(vector.x)
        
        if abs_shift_x >= abs_shift_y:
            vector.y /=abs_shift_x
            vector.x /=abs_shift_y
        else:
            vector.x /=abs_shift_y
            vector.y /= abs_shift_y
        
        print(vector.x, vector.y)
        
        S = abs_shift_x + abs_shift_y
                
        rect = pygame.Rect(rect)
        rect.center = [*self.pos1]
        point = [*self.pos1]
        covered_distance = [0, 0]
        
        while not obj.colliderect(rect) and S>0:
            S -= abs(vector.x) + abs(vector.y)
            point[0] += vector.x
            point[1] += vector.y
            covered_distance[0] += vector.x
            covered_distance[1] += vector.y
            rect.center = [*point]
        
        left_side = [
            rect.topleft,
            rect.midleft,
            rect.bottomleft
        ]
        right_side = [
            rect.topright,
            rect.midright,
            rect.bottomright
        ]
        bottom_side = [
            rect.bottomleft,
            rect.midbottom,
            rect.bottomright
        ]
        top_side = [
            rect.topright,
            rect.midtop,
            rect.topleft
        ]
        
        if self.side_collide(obj, left_side) or self.side_collide(obj, right_side):
            corrector = [-1, 1]
        elif self.side_collide(obj, bottom_side) or self.side_collide(obj, top_side):
            corrector = [1, -1]
        else:
            corrector = [1, 1]
        point = (rect.centerx, rect.centery)
        
        return point, *corrector, *covered_distance