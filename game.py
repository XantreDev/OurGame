import sys
import time
from math import floor

import pygame

from characters_classes.enemy import Enemy
from characters_classes.player import Player
from env_classes.level import level
from screen import screen
from tools.utils import spawn_generator


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
                self.add_char(Enemy(cord=spawn_generator(),
                                    player=self.characters[0], Worker=self))
            if self.timer > 1000:
                self.timer = 0
            self.timer += 1
        sys.exit()

    def delete_char(self, char):
        i = 0
        while i < len(self.characters):
            if self.characters[i] is char:
                del self.characters[i]
                return
            else:
                i += 1

        # self.delete_char.append(char)

    # def character_control(self):
    #     while self.delete_char:
    #         i = 0
    #         len_ = len(self.characters)
    #         while i < len_:
    #             if self.characters[i] is self.delete_char[0]:
    #                 del self.characters[i]
    #                 del self.delete_char[0]
    #                 len_-=1
    #                 if not self.delete_char: return
    #             i+=1

    def objects_control(self):
        i = int(0)
        while i < len(self.Objects):
            if self.Objects[i].off_frame:
                del self.Objects[i]
            else:
                i += 1

    def add_char(self, char):
        self.characters.append(char)

    def add_object(self, _object):
        self.Objects.append(_object)


def main():
    Worker().run()
