import random
from math import cos, pi, sin, radians

import pygame
from pygame.sprite import collide_rect

from characters_classes.deafult_object import GameObject
from object_classes.temp_object import TemporaryObject
from tools.route import Route
from tools.utils import Vector
import settings


class Bullet(TemporaryObject):
    bullet_color = (0, 0, 0)

    def __init__(self, cord=(0, 0), rotation=100, speed=20, durability=100, damage = 5, creator=None):
        # print(cord)
        super().__init__(cord, settings.bullet_size, color=self.bullet_color)
        self.rot_to_speed(rotation, speed)
        self.speed = speed
        self.off_frame = False
        self.route = Route()
        self.durability = durability
        self.creator = creator
        self.collide_count = 0
        self.damage = damage

    def rot_to_speed(self, rotation, speed):
        rotation = 360 - rotation

        rad = radians(rotation)

        self.shift_x = speed * cos(rad)
        self.shift_y = -1 * speed * sin(rad)

    def run(self, level_objects, characters):
        super().run()
        self.route.update((self.rect.centerx, self.rect.centery),
                          (self.rect.centerx + self.shift_x,
                           self.rect.centery + self.shift_y))
        self.rect.centerx += self.shift_x
        self.rect.centery += self.shift_y

        self.collide(level_objects)
        self.collide_with_characters(characters)

        if self.timer > 2:
            self.liveability_check()

    def collide_handler(self, obj):
        col_pos, k1, k2, d1, d2 = self.route.collide(self.rect, obj, Vector(self.shift_x,
                                                                            self.shift_y))

        self.shift_x *= k1
        self.shift_y *= k2

        self.rect.center = col_pos

        self.rect.centerx += self.shift_x - d1
        self.rect.centery += self.shift_y - d2

    def collide(self, objects): #TODO: переделать коллизии
        for obj in objects:
            if obj.colliderect(self.rect):
                self.collide_handler(obj)
                self.collide_count += 1

    def collide_with_characters(self, characters):
        self.route.collide_with_characters(self.rect, 
                                           characters,
                                           self.creator,
                                           self.damage)

    def liveability_check(self):
        if self.collide_count > self.durability:
            self.off_frame = True

    def draw(self, screen):
        super().draw(screen)
        if ((self.timer > 10 and self.timer % 2 == 0)
            and ((0 > self.rect.centerx or self.rect.centerx > screen.get_width())
                 or (0 > self.rect.centery or self.rect.centery > screen.get_height()))):
            self.off_frame = True
