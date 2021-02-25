import pygame
import random

colors = [(81,25,250),(175,45,180)]

class lvl:
    def __init__(self):
        self.objects = list()
        self.color = list()
        random.seed()
        self.import_all()

    def import_all(self):
        with open('levels/level/lvl1.txt','r') as f:
            while f:
                string = f.readline()
                if string=='': break
                string = string.strip().split(' ')
                if len(string)==4: self.objects.append(pygame.Rect(int(string[0]),int(string[1]),int(string[2]), int(string[3])))
            for i in range(len(self.objects)):
                self.color.append(colors[random.randint(0,len(colors)-1)])

    def draw(self, screen):
        for i in range(len(self.objects)):
            pygame.draw.rect(screen, self.color[i],self.objects[i])