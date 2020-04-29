import pygame
import random
from math import sin, cos, pi


class bullet():
    def __init__(self, cord=(0, 0), rotation=100, speed=20):
        print(cord)
        self.rect = pygame.Rect((cord[0], cord[1]), (2, 2))
        self.rot_to_speed(rotation, speed)

    def rot_to_speed(self, rotation, speed):
        angle = round(360 - rotation) % 90

        print(angle)

        shift_x = speed * cos((180 * angle) / pi)
        shift_y = speed * sin((180 * angle) / pi)

        if (rotation > 180):
            shift_y *= -1
        if (rotation > 90 and rotation < 270):
            shift_x *= -1

        self.shift_x = shift_x
        self.shift_y = shift_y

    def run(self):
        self.rect.centerx += self.shift_x
        self.rect.centery += self.shift_y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
