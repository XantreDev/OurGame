import pygame
import random

colors = [(121,196,113),(141,207,244)]

class lvl:
    def __init__(self):
        self.objects = list()
        self.color = list()
        random.seed()
        self.import_all()

    def import_all(self):
        with open('levels/level/lvl1.txt','r') as f:
            while f:
                str = f.readline()
                if str=='': break
                str = str.strip().split(' ')
                if len(str)==4: self.objects.append(pygame.Rect(int(str[0]),int(str[1]),int(str[2]), int(str[3])))
            for i in range(len(self.objects)):
                self.color.append(colors[random.randint(0,len(colors)-1)])

    def draw(self, screen):
        for i in range(len(self.objects)):
            pygame.draw.rect(screen, self.color[i],self.objects[i])