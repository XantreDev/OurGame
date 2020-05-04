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
        self.work=True
        self.S = screen()
        self.Objects = []
        self.Characters = [Player(Worker=self)]
        self.enemy = Enemy(Worker=self)
        self.L = level()
        self.timer = 0
    
    def run(self):
        for_fps = pygame.time.Clock()
        while self.work==True:
            for_fps.tick()
            timing = time.time()
            events_array = list()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.work = False
                elif event.type == pygame.KEYDOWN and chr(event.key) == 'o':
                    self.L.level_creator(self.S.return_screen())
                else: events_array.append(event)
            
            for item in self.Objects:
                item.run(self.L.objects)
            
            for item in self.Characters:
                item.logic(self.L, events_array)
            
            self.enemy.run(self.Characters[0], self.L.objects)
            
            self.L.draw(self.S.screen)
            
            self.S.drawing(self.Characters, self.Objects, self.L)
            
            self.enemy.draw(self.S.screen)
            wait = 13 - (time.time()-timing)*1000
            pygame.display.flip()
            if wait>0:
                pygame.time.wait(floor(wait))
            
            print(for_fps.get_fps())
            
            if self.timer % 40 == 0 or (wait < -3 and self.timer % 5 == 0):
                print(len(self.Objects))
                self.objects_control()
            if self.timer > 1000:
                self.timer = 0
            self.timer+=1
        sys.exit()
    
    def objects_control(self):
        i = int(0)
        while i < len(self.Objects):
            if self.Objects[i].off_frame:
                del self.Objects[i]
            else: 
                i+=1
                
    
    def object_adder(self, _object):
        self.Objects.append(_object)

def main():
    Worker().run()
