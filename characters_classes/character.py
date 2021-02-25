import pygame
import math
from os.path import normpath, normcase
from env_classes.weapons import AutoShotgun, AutomaticGun, SemiautomaticGun, Shotgun
from characters_classes.deafult_object import GameObject
from tools.utils import side_collide
from interface.health import HpInterface
from object_classes.blood import Blood
from object_classes.heal import HealObject


class character(GameObject):
    def __init__(self, hp=100, ammo=100, x=600, y=800, size=40, speed=10,
                 img=normpath('resources/images/character/Bob.png'), Worker=None,
                 weapon=AutomaticGun):
        # pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.ammo = ammo
        self.path = img
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.image = pygame.transform.rotate(self.image, 270)
        self.image_rotated = list()
        rect = self.image.get_rect()
        super().__init__(rect)
        self.rect.center = (400, 800)
        self.shift_x = 0
        self.shift_y = 0
        self.speed = speed
        self.a = 0
        self.all_rotates()
        self.collide_x = False
        self.collide_y = False
        self.worker = Worker
        self.weapon = weapon(Worker=self.worker, Character=self)
        self.hp_indicator = HpInterface(self)
        self.alive = True

    def heal(self):
        self.hp_modifier(20)

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

    def death(self):
        self.worker.add_object(HealObject(
            (self.rect.center), Worker=self.worker))
        self.alive = False

    def hp_modifier(self, dhp):
        self.hp += dhp if self.hp + dhp >= 0 and self.hp + dhp <= 100 else 0
        if self.hp == 0:
            self.death()

    def stop_move(self):
        self.shift_x, self.shift_y = 0, 0

    def hit(self, damage, vector):
        self.worker.add_object(Blood((self.rect.x, self.rect.y), self.worker))
        self.hp_modifier(-damage)
        self.move(vector.x, vector.y)
        self.hp_indicator.update()

    def process_logic(self, level):
        self.speed_correction()
        x, y = self.rect.centerx, self.rect.centery
        self.move(self.shift_x, self.shift_y)
        self.collide(level.objects)
        if (self.collide_x):
            self.rect.centerx = x
        if (self.collide_y):
            self.rect.centery = y
        self.rotation()

    def collide_with_lvl(self, objects):
        self.collide_x = False
        self.collide_y = False
        
        for item in objects:
            if side_collide(item, self.top_side()) or side_collide(item, self.bottom_side()):
                self.collide_y = True
            if side_collide(item, self.left_side()) or side_collide(item, self.right_side()):
                self.collide_x = True

    def logic(self, map, events=None):
        self.control_logic()
        self.process_logic(map)
        self.weapon.run()
        self.hp_indicator.update()

    def collide(self, level_objects):
        self.collide_with_lvl(level_objects)

    def rotation(self):  # будет работать на логике наведения прицела у противников
        pass

    def draw(self, screen):
        self.hold_at_screen(screen)
        screen.blit(self.image, self.rect)
        self.hp_indicator.draw(screen)
