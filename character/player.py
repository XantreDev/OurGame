import pygame
import math


pygame.init()
color = (73,24,19)

class character(pygame.sprite.Sprite):
    def __init__(self, hp = 100, ammo=100, x=600, y=800, size=40, speed = 10, img= 'Bob.png'):
        pygame.sprite.Sprite.__init__(self)
        self.hp=hp
        self.ammo=ammo
        self.image = pygame.image.load('character/Bob.png')
        self.image = pygame.transform.scale(self.image,(60,40))
        self.image = pygame.transform.rotate(self.image, 270)
        self.image_rotated = list()
        self.rect = self.image.get_rect()
        self.rect.center = (800,600)
        self.shift_x = 0
        self.shift_y = 0
        self.peeling_x = 0
        self.peeling_y = 0
        self.speed = speed
        self.a=0
        self.all_rotates()

    def all_rotates(self):
        x = pygame.image.load('character/Bob.png')
        x = pygame.transform.scale(x,(60,40))
        for i in range (0,721):
            self.image_rotated.append(pygame.transform.rotate(x, i/2))

    def control_logic(self, event):
        if event.type == pygame.KEYDOWN:
            if chr(event.key) == 'a':
                self.shift_x = -self.speed
            elif chr(event.key) == 'd':
                self.shift_x = self.speed
            if chr(event.key) == 'w':
                self.shift_y = -self.speed
            elif chr(event.key) == 's':
                self.shift_y = self.speed
        elif event.type == pygame.KEYUP:
            if chr(event.key) == 'a':
                self.shift_x = 0
            elif chr(event.key) == 'd':
                self.shift_x = 0
            if chr(event.key) == 'w':
                self.shift_y = 0
            elif chr(event.key) == 's':
                self.shift_y = 0
        if event.type == pygame.MOUSEMOTION:
            x,y=event.pos
            x1,y1 = self.rect.center
            #len = ((x1**2-x**2)**0.5 + (y1**2 - y**2))**0.5
            #if (x1-x)<=0:
            #    if (y1-y)<=0:
            #        math.atan()
            angle=round(math.degrees(math.atan2(y1-y,x1-x)+3.14159265))
            print(angle)
            if (angle != self.a):
                 self.image = self.image_rotated[(180-angle)*2]
                 self.a = angle
                 #self.rect = self.image.get_rect()
                 #self.rect.center = (x1,y1)
    # def collide_with_map(self, map):
    #     if self.collide_mask(map):
    #         self.shift_x = 0
    #         self.shift_y = 0

    def collide_with_lvl(self,lvl):
        for item in lvl.objects:
            if item.colliderect(self.rect):
                self.peeling_x = self.shift_x * -1
                self.peeling_y = self.shift_y * -1

    def collide(self, lvl):
        self.collide_with_lvl(lvl)

    def process_logic(self):
        self.rect.centerx +=self.shift_x + self.peeling_x
        self.rect.centery += self.shift_y + self.peeling_y
        self.peeling_x, self.peeling_y = 0,0

    def draw(self, screen):
        screen.blit(self.image,self.rect)
