import pygame
import sys
from characters_classes.player import Player
from screen import screen
from env_classes.level import level

class Worker:
    def __init__(self):
        pygame.init()
        self.work=True
        self.S = screen()
        self.Objects = []
        self.Characters = [Player(Worker=self)]
        self.L = level()
    
    def run(self):
        while self.work==True:
            events_array = list()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.work = False
                elif event.type == pygame.KEYDOWN and chr(event.key) == 'o':
                    self.L.level_creator(self.S.return_screen())
                else: events_array.append(event)
            
            for item in self.Objects:
                item.run()
            
            for item in self.Characters:
                item.logic(self.L, events_array)
            
            self.S.drawing(self.Characters, self.Objects, self.L)
            pygame.display.flip()
            pygame.time.wait(10)
        sys.exit()
    
    def object_adder(self, _object):
        self.Objects.append(_object)

def main():
    Worker().run()
    