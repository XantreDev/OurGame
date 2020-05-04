import pygame
from pygame.sprite import collide_rect

import settings
from characters_classes.deafult_object import GameObject
from tools.utils import Point, Vector, route_to_vector, side_collide


class Route:
    def __init__(self, pos1= (0, 0), pos2 = (0, 0)):
        self.pos1 = pos1
        self.pos2 = pos2

    def update(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def instant_vector(self, vector):
        abs_shift_x = vector.abs_x()
        abs_shift_y = vector.abs_y()
        
        if abs_shift_x == 0 or abs_shift_y == 0:
            if abs_shift_x == 0:
                return Vector(0, 1)
            return Vector(1, 0)
                
        if abs_shift_x >= abs_shift_y:
            return Vector(vector.x / abs_shift_x, vector.y / abs_shift_x)
        else:
            return Vector(vector.x / abs_shift_y, vector.y / abs_shift_y)

    def collide(self, rect, obj, vector):  # TODO: refactor        
        inst_vector = self.instant_vector(vector)

        S = vector.abs_x() + vector.abs_y()

        rect = pygame.Rect(rect)
        rect.center = [*self.pos1]
        point = [*self.pos1]
        covered_distance = [0, 0]

        while not obj.colliderect(rect) and S > 0:
            S -= inst_vector.abs_x() + inst_vector.abs_y()
            point[0] += inst_vector.x
            point[1] += inst_vector.y
            covered_distance[0] += inst_vector.x
            covered_distance[1] += inst_vector.y
            rect.center = [*point]
        
        game_object = GameObject(rect)
        
        corrector = self.corrector_execute(game_object, obj)
        
        point = (rect.centerx, rect.centery)

        return point, *corrector, *covered_distance
    
    def collide_with_characters(self, rect, characters, creator, damage):
        vector = route_to_vector(self)
        S = vector.abs_x() + vector.abs_y()
        vector = self.instant_vector(vector)
        
        vector.y *= 10
        vector.x *= 10
        
        into = [creator]
        
        point = [*self.pos1]
        rect = pygame.Rect(rect)
        
        while S > 0:
            S -= vector.abs_x() + vector.abs_y()
            point[0] += vector.x
            point[1] += vector.y
            rect.center = [*point]
            for item in characters:
                if item not in into and rect.colliderect(item):
                    item.hit(damage, vector / 4)
                    into.append(item)
            
            if len(into) == len(characters):
                return
        
    
    def corrector_execute(self, game_object, obj):
        if side_collide(obj, game_object.left_side()) or side_collide(obj, game_object.right_side()):
            return [-1, 1]
        elif side_collide(obj, game_object.bottom_side()) or side_collide(obj, game_object.top_side()):
            return [1, -1]
        else:
            return [-1, -1]
    
    @property
    def S(self):
        return abs(self.pos1[0] - self.pos2[0]) + abs(self.pos1[1] - self.pos2[1])
    
    def roadblocks(self, objects):
        vector = self.instant_vector(route_to_vector(self))
        vector.y *= (settings.precision // 3)
        vector.x *= (settings.precision // 3)
        point = Point(self.pos1[0], self.pos1[1])
        S = self.S
        while S > 0:
            for obj in objects:
                if obj.collidepoint(point.as_tuple()):
                    return True
            point.move(vector.x, vector.y)
            # print(point.as_tuple())
            S -= vector.abs_x() + vector.abs_y()
        return False
