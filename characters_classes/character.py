import pygame
import math
from os.path import normpath, normcase


class character(pygame.sprite.Sprite):
    def __init__(self, hp=100, ammo=100, x=600, y=800, size=40, speed=10, img=normpath('resources/images/character/Bob.png'), Worker=None):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.ammo = ammo
        self.path = img
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.image = pygame.transform.rotate(self.image, 270)
        self.image_rotated = list()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 800)
        self.shift_x = 0
        self.shift_y = 0
        self.speed = speed
        self.a = 0
        self.all_rotates()
        self.collide_x = False
        self.collide_y = False
        self.worker = Worker

    def control_logic(self):
        pass

    def all_rotates(self):
        x = pygame.image.load(self.path)
        x = pygame.transform.scale(x, (60, 50))
        for i in range(0, 721):
            self.image_rotated.append(pygame.transform.rotate(x, i/2))

    def speed_correction(self):
        if (abs(self.shift_x) == abs(self.shift_y) == self.speed):
            k_x = self.shift_x // abs(self.shift_x)
            k_y = self.shift_y // abs(self.shift_y)
            tmp = abs(self.speed) / 2**0.5
            self.shift_y = tmp * k_y
            self.shift_x = tmp * k_x

    def process_logic(self, lvl):
        self.speed_correction()
        x, y = self.rect.centerx, self.rect.centery
        self.rect.centerx += self.shift_x
        self.rect.centery += self.shift_y
        self.collide(lvl)
        if (self.collide_x):
            self.rect.centerx = x
        if (self.collide_y):
            self.rect.centery = y
        self.rotation()

    def collide_with_lvl(self, lvl):
        self.collide_x = False
        self.collide_y = False
        for item in lvl.objects:
            if (item.collidepoint(self.rect.midtop) or item.collidepoint(self.rect.midbottom) or item.collidepoint(self.rect.topleft) or
                    item.collidepoint(self.rect.bottomleft) or item.collidepoint(self.rect.topright) or item.collidepoint(self.rect.bottomright)):
                self.collide_y = True
            if (item.collidepoint(self.rect.midleft) or item.collidepoint(self.rect.midright) or item.collidepoint(self.rect.bottomleft)
                    or item.collidepoint(self.rect.topright) or item.collidepoint(self.rect.bottomright) or item.collidepoint(self.rect.topleft)):
                self.collide_x = True

    def logic(self, map, events=None):
        self.control_logic()
        self.process_logic(map)

    def collide(self, lvl):
        self.collide_with_lvl(lvl)

    def rotation(self):  # будет работать на логике наведения прицела у противников
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
