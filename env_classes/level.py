import random
from os.path import normcase, normpath

import pygame

colors = [(121, 196, 113), (141, 207, 244)]


class level:
    def __init__(self):
        self.objects = list()
        self.color = [(121, 196, 113), (141, 207, 244)]
        random.seed()
        self.import_all()
        self.x1, self.x2, self.y1, self.y2 = 0, 0, 0, 0
        self.checker = [False, False]
        self.field_creator()

    def import_all(self) -> None:
        """
        Level objects import from file
        """
        with open(normpath('levels/level/lvl1.txt'), 'r') as f:
            while f:
                string = f.readline()
                if string == '':
                    break
                string = string.strip().split(' ')
                if len(string) == 4:
                    self.objects.append(pygame.Rect(int(string[0]), int(
                        string[1]), int(string[2]), int(string[3])))
            for i in range(len(self.objects)):
                self.color.append(colors[random.randint(0, len(colors)-1)])

    def level_write(self, file):
        for item in self.objects:
            file.write(str(item.x) + ' ' + str(item.y) + ' ' +
                       str(item.h) + ' ' + str(item.w) + '\n')

    def level_creator(self, screen: pygame.Surface) -> None:
        """        
        Level Creator tool.
        
        Crates and write level in file.
        
        Screen - surface object.
        """
        self.name = input()
        f = open(normpath(self.name), 'w')
        work = True
        while work == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    work = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.x1, self.y1 = event.pos
                    self.checker[0] = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.x2, self.y2 = event.pos
                    self.checker[1] = True
                if event.type == pygame.KEYDOWN and chr(event.key) == 'o':
                    self.level_write(f)
                    work = False
            if self.checker[0] == self.checker[1] == True:
                if self.x1 > self.x2 and self.y1 > self.y2:
                    self.y1, self.y2, self.x1, self.x2 = self.y2, self.y1, self.x2, self.x1
                elif self.x1 > self.x2 and self.y1 < self.y2:
                    self.x1, self.x2 = self.x2, self.x1
                elif self.x1 < self.x2 and self.y1 > self.y2:
                    self.y1, self.y2 = self.y2, self.y1
                self.objects.append(pygame.Rect(self.x1, self.y1, abs(
                    self.x2-self.x1), abs(self.y2-self.y1)))
                self.checker[0], self.checker[1] = False, False
            self.draw(screen)
    
    # precision - точность заполнения матрицы, то есть при значении равном size[0 либо 1 в зависимости от того куда надо подставить] будет воссоздана картинка уровня в размере
    def field_creator(self, size=(1600, 900), precision=80) -> None:
        """
        Creates two-dimensional array of level.
        """
        # size[0] - строк; size[1] - столбцов
        # 80 - оптимальное значение на данный момент
        with open(normpath('levels/level/lvl1' + '_field.py'), 'w') as f:
            f.write('Field = [' + '\n')
            for i in range(0, size[0], size[0]//precision):
                buf_mas = list()
                for j in range(0, size[1], size[1]//precision):
                    tmp = False
                    for item in self.objects:
                        if (item.collidepoint(i, j)):
                            tmp = True
                            break
                    if tmp:
                        buf_mas.append(-1)
                    else:
                        buf_mas.append(0)
                f.write('   '+str(buf_mas) + ',\n')
            f.write(']')

    def draw(self, screen):
        for i in range(len(self.objects)):
            pygame.draw.rect(screen, self.color[0], self.objects[i])
