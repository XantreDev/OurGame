import pygame
import random

colors = [(121,196,113),(141,207,244)]

class level:
    def __init__(self):
        self.objects = list()
        self.color = [(121,196,113),(141,207,244)]
        random.seed()
        self.import_all()
        self.x1,  self.x2, self.y1, self.y2 = 0,0,0,0
        self.checker = [False, False]

    def import_all(self):
        with open('levels/level/lvl1.txt','r') as f:
            while f:
                str = f.readline()
                if str=='': break
                str = str.strip().split(' ')
                if len(str)==4: self.objects.append(pygame.Rect(int(str[0]),int(str[1]),int(str[2]), int(str[3])))
            for i in range(len(self.objects)):
                self.color.append(colors[random.randint(0,len(colors)-1)])

    def level_write(self, file):
         for item in self.objects:
            file.write(str(item.x) +' ' + str (item.y) + ' ' + str(item.h) + ' ' + str(item.w) + '\n')

    def level_creator(self,screen):
        self.name = input()
        f = open(self.name,'w')
        work = True
        while work == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    work = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.x1,self.y1 = event.pos
                    self.checker[0] = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.x2,self.y2 = event.pos
                    self.checker[1] = True
                if event.type == pygame.KEYDOWN and chr(event.key) == 'o':
                    self.level_write(f)
                    work = False
            if self.checker[0] == self.checker[1] == True:
                if self.x1 > self.x2 and self.y1 > self.y2:
                    self.y1,self.y2,self.x1,self.x2 = self.y2,self.y1,self.x2,self.x1
                elif self.x1 > self.x2 and self.y1 < self.y2:
                    self.x1,self.x2 = self.x2,self.x1
                elif self.x1 < self.x2 and self.y1 > self.y2:
                    self.y1,self.y2 = self.y2,self.y1
                self.objects.append(pygame.Rect(self.x1,self.y1,abs(self.x2-self.x1),abs(self.y2-self.y1)))
                self.checker[0], self.checker[1] = False, False
            self.draw(screen)

    def draw(self, screen):
        for i in range(len(self.objects)):
            pygame.draw.rect(screen, self.color[0],self.objects[i])
        pygame.display.flip()
        pygame.time.wait(10)