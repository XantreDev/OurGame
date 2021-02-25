import pygame
import math
from characters_classes.character import character
from object_classes.bullet import Bullet
import settings


color = (73, 24, 19)


class Player(character):
    def __init__(self, hp=100, ammo=100, x=600, y=800, size=40, speed=10, img='Bob.png', Worker=None):
        super().__init__(Worker=Worker)
        self.mouse_pos = (0, 0)
        self.block = (0, 0)
        
    def control_logic(self, events=None):
        if events is None:
            events = list()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == 'a':
                    self.shift_x = -self.speed
                if chr(event.key) == 'd':
                    self.shift_x = self.speed
                if chr(event.key) == 'w':
                    self.shift_y = -self.speed
                if chr(event.key) == 's':
                    self.shift_y = self.speed
            elif event.type == pygame.KEYUP:
                if chr(event.key) == 'a':
                    self.shift_x = 0
                if chr(event.key) == 'd':
                    self.shift_x = 0
                if chr(event.key) == 'w':
                    self.shift_y = 0
                if chr(event.key) == 's':
                    self.shift_y = 0
            if event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.weapon.activate()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.weapon.deactivate()

    def angle(self):
        return (math.degrees(
            math.atan2(self.rect.centery - self.mouse_pos[1], self.rect.centerx - self.mouse_pos[0]) + math.pi))

    def rotation(self):
        angle = self.angle()
        if (round(angle * 2) != round(self.a * 2)):
            self.image = self.image_rotated[(180 - round(angle)) * 2]
            self.a = angle
        # print(self.a)

    def hit(self, *args):
        arg = args[0]
        # self.hp_modifier(-arg)

    def logic(self, map, events):
        self.control_logic(events)
        self.process_logic(map)
        self.weapon.run()
        self.hp_indicator.update()
        self.update_block()
    
    def update_block(self):
        self.block = (self.rect.centerx // settings.precision, self.rect.centery // settings.precision)


    def draw(self, screen):
        self.hold_at_screen(screen)
        screen.blit(self.image, self.rect)
        self.hp_indicator.draw(screen)
