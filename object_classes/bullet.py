import pygame
import random
from math import sin, cos, pi


class bullet():
    def __init__(self, cord=(0, 0), rotation=100, speed=20):
        print(cord)
        self.rect = pygame.Rect((cord[0], cord[1]), (3, 3))
        self.rot_to_speed(rotation, speed)

    def rot_to_speed(self, rotation, speed):
        rotation = 360 - rotation
        print(rotation)
        
        rad = (pi * rotation) / 180
        
        self.shift_x = speed * cos(rad)
        self.shift_y = -1 * speed * sin(rad)

    def run(self):
        self.rect.centerx += self.shift_x
        self.rect.centery += self.shift_y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
