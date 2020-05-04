import sys
import time
from math import floor

import pygame

from characters_classes.enemy import Enemy
from characters_classes.player import Player
from env_classes.level import level
from screen import screen


class Worker:
    def __init__(self):
        pygame.init()
        self.work = True
        self.S = screen()
        self.Objects = []
        self.characters = [Player(Worker=self)]
        self.characters.append(Enemy(player=self.characters[0], Worker=self))
        self.L = level()
        self.timer = 0

    def run(self):
        for_fps = pygame.time.Clock()
        while self.work == True:
            for_fps.tick()
            timing = time.time()
            events_array = list()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.work = False
                elif event.type == pygame.KEYDOWN and chr(event.key) == 'o':
                    self.L.level_creator(self.S.return_screen())
                else:
                    events_array.append(event)

            for item in self.Objects:
                item.run(self.L.objects, self.characters)
            
            self.characters[0].logic(self.L, events_array)
            
            for i in range(1, len(self.characters)):
                item = self.characters[i]
                item.run(self.L.objects)

            self.L.draw(self.S.screen)

            self.S.drawing(self.characters, self.Objects, self.L)

            wait = 16 - (time.time()-timing)*1000
            pygame.display.flip()
            if wait > 0:
                pygame.time.wait(floor(wait))

            # print(for_fps.get_fps())

            if self.timer % 80 == 0:
                print(len(self.Objects))
                self.objects_control()
            if self.timer > 1000:
                self.timer = 0
            self.timer += 1
        sys.exit()

    def objects_control(self):
        i = int(0)
        while i < len(self.Objects):
            if self.Objects[i].off_frame:
                del self.Objects[i]
            else:
                i += 1

    def add_object(self, _object):
        self.Objects.append(_object)


def main():
    Worker().run()
