import pygame

class Route:
    def __init__(self):
        self.pos1 = (0, 0)
        self.pos2 = (0, 0)
    
    def update(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
    
    def collide(self, rect, obj, vector):
        rect = pygame.Rect(rect)
        rect.center = [*self.pos1]
        point = [*self.pos1]
        covered_distance = [0, 0]
        
        while not obj.colliderect(rect):
            point[0] += vector.x
            point[1] += vector.y
            covered_distance[0] += vector.x
            covered_distance[1] += vector.y
            rect.center = [*point]
        
        corrector = [1, 1]
        
        if (obj.collidepoint(rect.midtop) or obj.collidepoint(rect.midbottom) or obj.collidepoint(rect.topleft) or
            obj.collidepoint(rect.bottomleft) or obj.collidepoint(rect.topright) or obj.collidepoint(rect.bottomright)):
            corrector[0] *= -1
        if (obj.collidepoint(rect.midleft) or obj.collidepoint(rect.midright) or obj.collidepoint(rect.bottomleft)
            or obj.collidepoint(rect.topright) or obj.collidepoint(rect.bottomright) or obj.collidepoint(rect.topleft)):
            corrector[1] *= -1
        
        point = (rect.centerx, rect.centery)
        
        return point, *corrector, *covered_distance